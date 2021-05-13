import sys
input = sys.stdin.readline
N = int(input())
a = []
for _ in range(N): a.append(int(input()))
if a[0] != 0:
  print(-1)
  exit(0)
for i in range(N - 1):
  if a[i + 1] > a[i] and (a[i + 1] - a[i] > 1):
    print(-1)
    exit(0)
res = 0
s = 0
x = 1
for i in range(1, N):
  if a[i] == x:
    s += 1
  else:
    if x > 0: res += (s - 1) * x + 1
    if x > a[i] and a[i] > 1:
      res += a[i] - 1
    s = 1
    x = a[i]
  #print(i, res)
if x > 0: res += (s - 1) * x + 1
print(res)