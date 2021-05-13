N,K = list(map(int,input().split()))
X = list(map(int,input().split()))
ans = 10**10

for i in range(N-K+1):
    #S = X[i:i+K]
    #print(S,S[0],S[-1])
    mi = X[i]
    ma = X[i+K-1]
    #print(mi,ma)
    if ma<=0:
        ans = min(ans ,abs(mi))
    elif  mi>0:
        ans = min(ans ,ma)
    elif  mi<0 and ma>0:
        if abs(mi) > ma :
            ans = min(ans,abs(mi) + 2*ma)
        else :
            ans = min(ans,abs(mi)*2 + ma)

print(ans)