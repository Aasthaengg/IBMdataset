n, k = map(int, input().split())
ans = ""
if n % 2 == 0:
  if n / 2 >= k:
    ans = "YES"
  else:
    ans = "NO"
else:
  if n // 2 + 1 >= k:
    ans = "YES"
  else:
    ans = "NO"
print(ans)