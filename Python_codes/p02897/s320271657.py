n=int(input())
cnt=0
ans=0
for i in range(1,n+1):
  cnt+=1
  if i%2==1:
    ans+=1
    
print(ans/cnt)