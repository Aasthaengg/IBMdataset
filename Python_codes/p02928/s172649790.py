n,k=map(int,input().split())
a=list(map(int,input().split()))
ca,cb=0,0
mod=10**9+7
for i,x in enumerate(a):
  for j,y in enumerate(a):
    if x>y:
      if i<j:ca+=1
      else:cb+=1
print((ca*k*(k+1)//2%mod+cb*k*(k-1)//2%mod)%mod)