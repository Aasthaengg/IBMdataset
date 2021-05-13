n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]
cnt=[0]*(n+1)
for i in range(m):
  cnt[ab[i][0]]+=1
  cnt[ab[i][1]]+=1
flag=True
for i in range(1,n+1):
  if cnt[i]%2!=0:flag=False
print('YES' if flag else 'NO')