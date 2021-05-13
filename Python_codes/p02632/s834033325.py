import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

mod = 10**9 + 7
k = int(input())
s = input()
n = len(s)

def make_tables(n, mod = 10 ** 9 + 7):
    fac = [1, 1] # 階乗テーブル
    finv = [1, 1] #逆元の階乗テーブル
    inv = [0, 1] #逆元テーブル

    for i in range(2, n + 1):
        fac.append((fac[-1] * i) % mod)
        inv.append((mod -inv[mod % i] * (mod // i)) % mod)
        finv.append((finv[-1] * inv[-1]) % mod)
    return fac, finv

def nCk(n, k, mod = 10 ** 9 + 7):
    k = min(k, n-k)
    return fac[n] * finv[k] * finv[n-k] % mod

##########################
fac, finv = make_tables(2*10**6 + 1)
ans = 0
for i in range(k + 1):
    temp = 1
    temp *= pow(26, i, mod)
    temp %= mod
    j = k - i
    temp *= pow(25, j, mod)
    temp %= mod
    temp *= nCk(n + j - 1, n - 1)
    ans += temp
    ans %= mod
print(ans % mod)



