N,K,*H=map(int,open(0).read().split())
ans=10**9
H.sort()
i=0
while i+K-1<N:
    ans=min(ans,H[i+K-1]-H[i])
    i+=1
print(ans)
