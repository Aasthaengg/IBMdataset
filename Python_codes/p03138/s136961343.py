import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = list(map(int, input().split()))
t = [0] * 41
x = 0
res = 0
for i in range(N):
  for j in range(41):
    t[j] += (a[i] & (1 << j)) > 0

tt = [[0] * 2 for _ in range(41)]
for i in range(41):
  tt[i][0] = t[i] * (1 << i)
  tt[i][1] = (N - t[i]) * (1 << i)
for i in range(40, -1, -1):
  if x + (1 << i) > K:
    res += tt[i][0]
    continue
  if tt[i][0] >= tt[i][1]:
    res += tt[i][0]
  else:
    res += tt[i][1]
    x += 1 << i
print(res)