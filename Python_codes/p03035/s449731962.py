a, b = map(int, input().split())
ans = 0
if 6 <= a <= 12:
  ans = b // 2
elif a > 12:
  ans = b
print(ans)
