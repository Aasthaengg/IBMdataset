n = int(input())
MOD = 10**9 + 7
u = pow(10, n, MOD)
v = pow(9, n, MOD)
w = pow(8, n, MOD)

print( (u - 2*v + w) % MOD)