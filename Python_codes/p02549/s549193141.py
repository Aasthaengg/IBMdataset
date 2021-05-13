N,K = map(int, input().split())
d = [0]*2*K
for i in range(K):
    d[2*i], d[2*i+1] = map(int, input().split())
a=[0]*(N+1)
b=[0]*(N+1)
a[1]=1
b[1]=1
for i in range(2,N+1):
    t=0
    for j in range(K):
        if i-d[2*j]>0:
            t+=b[i-d[2*j]]
        if i-d[2*j+1]-1>0:
            t-=b[i-d[2*j+1]-1]
    a[i]=t%998244353
    b[i]=(b[i-1]+a[i])
print(a[N])
