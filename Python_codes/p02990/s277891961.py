
n,k = map(int,input().split())
mod = 10**9+7
C=[[0] * (k+1) for i in range(n+1)]
for i in range(1,n+1):
    C[i][1] = i
    for j in range(2,k+1):
        C[i][j] = (C[i-1][j-1] + C[i-1][j])%mod
print(n-k+1)
for i in range(1,k):
    if n-k < i or k-1 < i:
        print(0)
        continue
    print((C[n-k+1][i+1] * C[k-1][i])%mod)
    # print(C[n-k+1][i] , C[k-1][i-1])
