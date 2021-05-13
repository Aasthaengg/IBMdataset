n,m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

MOD = 10**9+7

X_sum = 0
for i in range(n):
    X_sum += (2*i-n+1)*X[i]
    X_sum = X_sum % MOD
    
Y_sum = 0
for j in range(m):
    Y_sum += (2*j-m+1)*Y[j]
    Y_sum = Y_sum % MOD
    
print(X_sum * Y_sum % MOD)