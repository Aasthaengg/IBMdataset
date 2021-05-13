n,k=map(int,input().split())
k-=1
a=list(map(int, input().split()))
for i in range(n):
    if a[i]==1:
        index=i
print(-(-i//k)-(-(n-i-1)//k))