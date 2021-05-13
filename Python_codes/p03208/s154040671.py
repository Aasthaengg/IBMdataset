n,k=map(int,input().split())
a=sorted([int(input())for i in range(n)])
mim=10**9
for i in range(n-k+1):
    sa=a[i+k-1]-a[i]
    mim=min(mim,sa)
print(mim)
