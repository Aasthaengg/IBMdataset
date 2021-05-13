N,T=map(int, input().split())
ts=list(map(int, input().split()))
ts+=[10**12]
ans=0
for i in range(N):
    ans+=min(T,ts[i+1]-ts[i])
print(ans)