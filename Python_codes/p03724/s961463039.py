n,m=map(int,input().split())
ans=[0]*n
for i in range(m):
  a,b=map(int,input().split())
  ans[a-1]^=1
  ans[b-1]^=1
if 1 not in ans:print('YES')
else:print('NO')