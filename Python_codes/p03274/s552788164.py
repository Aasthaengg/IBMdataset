n,k=map(int,input().split())
x=list(map(int,input().split()))
k-=1
ans=float('inf')

for i in range(n-k):
  l,r=x[i],x[i+k]
  if l==0:
      ans=min(ans,r)
  
  elif r==0:
      ans=min(ans,abs(l))
  
  elif l<0 and r>0:
      ans=min(ans,abs(l)*2+r)
      ans=min(ans,abs(l)+2*r)
  
  elif l<0 and r<0:
      ans=min(ans,abs(l))
  
  elif l>0 and r>0:
      ans=min(ans,r)



print(ans)