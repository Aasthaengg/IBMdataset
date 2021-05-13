n,m,c = map(int, input().split())
b = list(map(int, input().split()))
a = [[] for h in range(n)]
s = 0
ans = 0
for i in range(n):
  a[i] = list(map(int, input().split()))
  for j in range(m):
    s += a[i][j]*b[j]
  if s + c > 0:
    ans += 1
  s = 0
print(ans)