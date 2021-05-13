x, y = map(int, input().split())
key = y//x
ans = 0
while key:
  ans += 1
  key //= 2
print(ans)