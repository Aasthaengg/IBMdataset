N,K=map(int,input().split())
H=list(map(int,input().split()))
H.sort(reverse=True)
ans=0
for i in range(N-K):
    ans+=H[K+i]
print(ans)