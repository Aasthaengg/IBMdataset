import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
x = a[-1]
y = 4
if x != 2:
  print(-1)
  exit(0)
for i in range(N - 2, -1, -1):
  p = a[i]
  t = -(-x // p)
  x = t * p
  u = -(-y // p)
  y = u * p
t = x + 0
for i in range(N):
  t -= t % a[i]
if t == 2:
  print(x, y - 1)
else: print(-1)