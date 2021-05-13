x,y=map(int,input().split())
lis=[0,300000,200000,100000]
lis=lis+[0]*1000
ans=lis[x]+lis[y]
if x==y==1:
  ans+=400000
print(ans)