x, y = list(map(int, input().split()))

ans = abs(abs(x) - abs(y))

if (x < 0) == (y > 0):
  ans += 1
elif (x > y):
  ans += 2

print(ans)