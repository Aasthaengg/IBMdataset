n,m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10**9+7

x_tmp = 0
for i in range(n):
    x_tmp += (2*i-n+1) * X[i]
y_tmp = 0
for i in range(m):
    y_tmp += (2*i-m+1) * Y[i]

print(x_tmp * y_tmp % mod)