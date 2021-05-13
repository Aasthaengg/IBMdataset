a, b, c = map(int, input().split())
if a + b + 1 >= c:
  ans = b + c
else:
  ans = b + a + b + 1
print(ans)