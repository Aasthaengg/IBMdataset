n, k = map(int, input().split())
ans = 0
if k == 1:
  ans = 0
else:
  ans = n - k
print(ans)