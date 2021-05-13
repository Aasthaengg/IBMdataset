N,K = map(int,input().split())
X = list(map(int,input().split()))

ans = float('inf')
for i in range(K-1,N):
    xl = X[i-K+1]
    xr = X[i]
    ans = min(abs(xr)+abs(xr-xl),abs(xl)+abs(xr-xl),ans)
print(ans)