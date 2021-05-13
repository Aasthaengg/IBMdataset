import sys
input = sys.stdin.readline
N, T = map(int, input().split())
a = list(map(int, input().split())) + [-N]
last = T
res = N
for t in range(N):
  x = T
  for i in range(T):
    if i == last: continue
    if a[x] <= a[i] and (a[i] > 0): x = i
  if x == T: x = last
  a[x] -= 1
  res -= x != last or (t == 0)
  last = x
print(res)