n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]
cnt = 0
for j in range (n):
  ans = 0
  for k in range (m):
    ans += a[j][k]*b[k]
  if ans+c > 0:
    cnt += 1
print(cnt)