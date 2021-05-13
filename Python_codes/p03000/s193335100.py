n,x=map(int,input().split())
l=list(map(int,input().split()))
z=0
ans=1
i=0
for i in range(n):
  z+=l[i]
  if z>x:
    break
  else:
    ans+=1
    
print(ans)