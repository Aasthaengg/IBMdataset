n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=1000000007
l1=0
l2=0
for i in range(n):
  for j in range(n):
    
    if i!=j:
      
      if a[i]>a[j]:
        l1+=1
        
        if i<j:
          l2+=1

k=k%mod
print((l2*k+l1*k*(k-1)//2)%mod)