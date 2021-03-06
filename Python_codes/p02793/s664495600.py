N = int(input())
A = [int(i) for i in input().split()]
MOD = 10**9 + 7

def gcd(n, m):
    if m == 0:
        return n
    while m != 0:
        n, m = m, n % m
    return n

def lcm(n, m):
    return n * m // gcd(n, m)

L = 1
for a in A:
    L = lcm(L, a)

ans = 0
for a in A:
    ans += L // a

print(ans % MOD)
