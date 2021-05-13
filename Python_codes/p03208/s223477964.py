N,K=map(int,input().split())
h=[int(input()) for i in range(N)]
s=sorted(h)
ans=10**10
for i in range(N-K+1):
    Z=s[i+K-1]-s[i]
    ans=min(ans,Z)
print(ans)