a,b=map(int,input().split())

ans=0
res=1
while res<b:
  res=res+a-1
  ans+=1
print(ans)