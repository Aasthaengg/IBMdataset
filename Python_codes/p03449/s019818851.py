n = int(input())
a = [list(map(int, input().split())) for i in range(2)]

res = 0
for i in range(n):
  ans = 0
  for j in range(i+1):
    ans += a[0][j]
  for k in range(i, n):
    ans += a[1][k]
    
  res = max(ans, res)
  
print(res)