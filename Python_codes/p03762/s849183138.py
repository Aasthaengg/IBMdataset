MOD = 10**9 + 7


n, m = map(int, input().split())
X = [int(i) for i in input().split()]
Y = [int(i) for i in input().split()]

Sx, Sy = 0, 0

for i in range(n-1):
    Sx += (X[i+1]-X[i])*(i+1)*(n-1-i)

for k in range(m-1):
    Sy += (Y[k+1]-Y[k])*(k+1)*(m-1-k)

print((Sx*Sy) % MOD)
