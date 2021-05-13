n, k = (int(x) for x in input().split())
c = {} 
t = 0
MOD = 1000000007
for x in range(k, 0, -1):
    q = k // x
    c[x] = pow(q, n, MOD) - sum(c[x * y] for y in range(2, q + 1))
    t += c[x] * x
    t = t % MOD
print(t)