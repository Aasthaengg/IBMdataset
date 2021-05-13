N=int(input())
C=[int(input()) for i in range(N)]
a=[0]*N
p={}
m=10**9+7
for i,c in enumerate(C):
    a[i]=a[i-1]
    if c in p and p[c]<i-1:
        a[i]=(a[i]+a[p[c]]+1)%m
    p[c]=i
print(a[-1]+1)