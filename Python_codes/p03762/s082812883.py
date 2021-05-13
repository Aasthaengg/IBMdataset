n, m = map(int, input().split())
*x, = map(int, input().split())
*y, = map(int, input().split())

acx = [0]*(n)
acy = [0]*(m)
acx2 = [0]*(n)
acy2 = [0]*(m)
MOD = 10**9+7

for i in range(1, n):
    acx2[i] = acx2[i-1]+i*(x[i]-x[i-1])
    acx2[i] %= MOD
for i in range(1, m):
    acy2[i] = acy2[i-1]+i*(y[i]-y[i-1])
    acy2[i] %= MOD

for i in range(1, n):
    acx[i] = (acx[i-1]+acx2[i])%MOD
for i in range(1, m):
    acy[i] = (acy[i-1]+acy2[i])%MOD

print(acx[-1]*acy[-1]%MOD)