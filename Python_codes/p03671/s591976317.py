import sys
sys.setrecursionlimit(int(1e6))

a, b, c = list(map(int, input().split()))

ans = 0
if a < b:
  ans = a
  if b < c:
    ans += b
  else:
    ans += c
else:
  ans = b
  if a < c:
    ans += a
  else:
    ans += c

print(ans)
