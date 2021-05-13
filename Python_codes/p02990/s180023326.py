import sys
N, K = map(int, input().split())
mod = 7 + 10 ** 9
fact = [1] * (N + 1)
for i in range(1, N + 1): fact[i] = (i * fact[i-1]) % mod
revfact = [1] * (N + 1)
revfact[N] = pow(fact[N], mod - 2, mod)
for i in reversed(range(1, N)): revfact[i] = (revfact[i+1] * (i + 1)) % mod

def comb(n, r):
    return (fact[n] * revfact[n-r] * revfact[r]) % mod

def solve():
    Ans = [0] * K
    for i in range(K):
        if i + 1 > N - K + 1: continue
        place = comb(N - K + 1, i + 1)
        rem = K - i - 1
        remPatt = comb(rem + i, i)
        Ans[i] = (place * remPatt) % mod
    print("\n".join(map(str, Ans)))

    return 0

if __name__ == "__main__":
    solve()