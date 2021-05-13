mod=10**9+7
n,k=map(int,input().split())
k1=(k*(k+1)//2)%mod
k2=(k*(k-1)//2)%mod
a=list(map(int,input().split()))
p=0
for i,j in enumerate(a):
    e=0
    for m in a[i:]:
        e+=j>m
    p=(p+(e*k1)%mod)%mod
for i,j in enumerate(a):
    e=0
    for m in a[:i]:
        e+=j>m
    p=(p+(e*k2)%mod)%mod
print(p)