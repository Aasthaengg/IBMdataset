N,M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

MOD = 10**9+7

x_diff = 0
y_diff = 0

for i in range(N):
    x_diff += (2*i-N+1)*X[i]%MOD
    
for i in range(M):
    y_diff += (2*i-M+1)*Y[i]%MOD
    
print(x_diff*y_diff%MOD)