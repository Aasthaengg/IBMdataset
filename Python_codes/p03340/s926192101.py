import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
xor = a[0]
sm = a[0]
r = 1
ans = 0
for l in range(n):
  if l == r:
    xor = a[r]
    sm = a[r]
    r += 1
  while sm == xor and r <= n-1:
    xor = xor^a[r]
    sm = sm+a[r]
    ans += r-l
    r += 1
  if sm == xor:
    ans += 1
  xor = xor^a[l]
  sm = sm-a[l]
print(ans)