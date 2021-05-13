N = int(input())
mod = 10**9 + 7
def inv(x):
    return pow(x, mod - 2, mod)
def comb(n, k):
    ue = 1
    shita = 1
    n %= mod
    for i in range(k):
        ue = ue * (n - i) % mod
        shita = shita * (i + 1) % mod
    return ue * inv(shita) % mod
if N == 1:
    print(0)
else:
    print((pow(10,N,mod)-2*pow(9,N,mod)+pow(8,N,mod))%mod)
