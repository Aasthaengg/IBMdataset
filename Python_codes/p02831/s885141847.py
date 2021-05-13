a,b=map(int,input().split())

ans=0
for i in range(1,a+1):
  if b%i==0:
    if a%i==0:
      ans=max(ans,i)
      
print((a*b)//ans)
