def Csum(a):
    b,c=[0],0
    for i in range(len(a)):
        c+=a[i]
        b.append(c)
    return b
n,k=map(int,input().split())
p=Csum(list(map(int,input().split())))
ans=0
for i in range(n-k+1):
    ans=max(ans,p[i+k]-p[i])
print((ans+k)/2)