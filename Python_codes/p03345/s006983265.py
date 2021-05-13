a, b, c, k = map(int, input().split())
ans = a-b
if k%2:
  ans *= -1
if abs(ans) >= pow(10,18):
  print("Unfair")
else:
  print(ans)