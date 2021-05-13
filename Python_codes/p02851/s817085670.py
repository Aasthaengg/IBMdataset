import numpy
N,K=map(int,input().split())

if K==1:
    print(0)
    exit(0)

A=list(map(int,input().split()))
S=[0]+list(numpy.cumsum(A)) #累積和
S2=[(S[i]-i)%K for i in range(N+1)]

d = {}
ans = 0
for j in range(1,N+1):
    if j>K-1:
        if S2[j-K] in d:
            d[S2[j-K]] -= 1
        
    if S2[j-1] in d:
        d[S2[j-1]] += 1
    else:
        d[S2[j-1]] = 1
        
    if S2[j] in d:
        ans += d[S2[j]]
print(ans)