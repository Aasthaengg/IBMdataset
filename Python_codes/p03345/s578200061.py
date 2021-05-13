a, b, c, k = map(int, input().split())
ans = 0
if k % 2 == 0:
  ans = a - b
else:
  ans = b - a
print(ans)