n, a, b = map(int, input().split())
ans = 0
if a > b:
  ans = 0
elif n == 1 and a != b:
  ans = 0
elif n == 1 and a == b:
  ans = 1
else:
  ans = (b - a) * (n - 2) + 1
print(ans)