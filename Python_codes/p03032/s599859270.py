N,K=map(int,input().split())
V = list(map(int,input().split()))

ans = -(10**9)
for A in range(0,K+1,1):
    for B in range(0,min(K,N)-A+1,1):
        tmp = V[0:A] + V[N-B:N]
        tmp.sort()
        for i in range(0,min(K-A-B,A+B),1):
            tmp[i]=max(tmp[i],0)
        ans = max(ans,sum(tmp))
print(ans)