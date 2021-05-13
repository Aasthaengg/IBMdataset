n,x=map(int,input().split())
l=list(map(int,input().split()))
a=0
i=0
ans=1
while a+l[i]<=x:
  ans+=1
  a=a+l[i]
  i+=1
  if i+1>n:
    break
print(ans)