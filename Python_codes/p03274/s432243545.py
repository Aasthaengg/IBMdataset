
N,K = list(map(int,input().split()))
X = list(map(int,input().split()))

Xrev = X[::-1]
ans = abs(X[0]-X[-1])+abs(X[0])+abs(X[-1])  
for i in range(N-K+1):
    Xdis = abs(X[i])+abs(X[i+K-1]-X[i])
    ans = min(ans,Xdis)
for i in range(N-K+1):
    Xdis = abs(Xrev[i])+abs(Xrev[i+K-1]-Xrev[i])
    ans = min(ans,Xdis)
print(ans)
