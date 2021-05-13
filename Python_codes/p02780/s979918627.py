n,k=map(int,input().split())
a=[int(s) for s in input().split()]
b=[0]*k
c=0
v=[0]*n
v[0]=a[0]
for i in range(n-1):
    v[i+1]=v[i]+a[i+1]
mx=v[k-1]
for i in range(k,n):
    g=v[i]-v[i-k]
    mx=max(mx,g)  
    
print((mx+k)/2)
