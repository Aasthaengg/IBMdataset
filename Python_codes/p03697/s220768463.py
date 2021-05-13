a, b = map(int, input().split())
abSum = a + b
if abSum >= 10:
  ans = "error"
else:
  ans = abSum
print(ans)