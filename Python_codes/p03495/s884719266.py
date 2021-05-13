n,k=map(int,input().split())
a=list(map(int,input().split()))
x=[0]*(2*10**5+1)
ans=0
for i in range(n):
    x[a[i]]+=1
z=[x[i] for i in range(2*10**5+1) if x[i]!=0]
z=sorted(z)
for i in range(max(len(z)-k,0)):
    ans+=z[i]
print(ans)
