MOD = 10**9 + 7
n, m = [int(item) for item in input().split()]
x = [int(item) for item in input().split()]
y = [int(item) for item in input().split()]

x_total, y_total = 0, 0 
for i in range(1,n):
    x_total += (i * (n-i) * (x[i] - x[i-1])) % MOD
for i in range(1,m):
    y_total += (i * (m-i) * (y[i] - y[i-1])) % MOD
print((x_total * y_total)%MOD)