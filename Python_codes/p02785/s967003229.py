n,k=map(int,input().split())
H=list(map(int,input().split()))
ans=0
if n<=k:
    print(0)
else:
    H.sort()
    H=H[0:n-k]
    for i in range(n-k):
        ans+=H[i]
    print(ans)