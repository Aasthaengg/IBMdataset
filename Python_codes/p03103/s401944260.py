n,m=map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[0])
now=0
ans=0
for i in range(n):
  if now+ab[i][1]<=m:
    now += ab[i][1]
    ans += ab[i][0]*ab[i][1]
  else:
    ans += ab[i][0]*(m-now)
    break
print(ans)