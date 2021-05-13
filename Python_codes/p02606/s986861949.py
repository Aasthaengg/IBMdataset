L, R, d = map(int, input().split())

x = L
ans = 0

while x<=R:
  if x % d == 0:
    ans += 1
  x += 1

print(ans)
