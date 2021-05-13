import sys
input = sys.stdin.readline
mod = 10**9 + 7
n, k = [int(x) for x in input().split()]
red = n - k
blue = k

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

fac, finv = make_tables(n)

for i in range(1, k + 1):
    red_, blue_ = red, blue
    red_ -= (i - 1)
    blue_ -= i
    if red_ < 0 or blue_ < 0:
        print(0)
        continue
    ans = nCk(blue_ + i - 1, i - 1) * nCk(red_ + i, i)
    print(ans % mod)
    


