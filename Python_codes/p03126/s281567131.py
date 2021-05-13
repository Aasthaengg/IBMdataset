n,m=map(int,input().split())
flg=[1]*m
for i in range(n):
  a=list(map(int,input().split()))[1:]
  for j in range(m):
    if j+1 not in a:
      flg[j]=0
print(sum(flg))