from math import gcd
MOD = 10**9 + 7
MOD_t_MAX = 2*(10**5) + 10

fac  = [None] * MOD_t_MAX
finv = [None] * MOD_t_MAX
inv  = [None] * MOD_t_MAX
def MOD_COM_init():
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, MOD_t_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
def MOD_COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    n = int(input())
    iwashi = [list(map(int, input().split())) for _ in range(n)]
    MOD_COM_init()
    ans = pow(2, n, MOD)
    ans -= 1
    ans %= MOD
    dic = {}
    cnt = [0, 0, 0, 0]
    for i in range(n):
        a, b = iwashi[i]
        if a == 0 and b == 0:
            cnt[3] += 1
        elif b == 0:
            cnt[2] += 1
        elif a == 0:
            cnt[1] += 1
        else:
            cnt[0] += 1
            fa, fb = False, False
            if a < 0:
                fa = True
                a *= -1
            if b < 0:
                fb = True
                b *= -1
            c = gcd(a, b)
            a //= c
            b //= c
            if (fa and not fb) or (not fa and fb):
                a *= -1
            tmp = (a, b)
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
    L = 1
    if 0 < cnt[3]:
        p = (pow(2, n-cnt[3], MOD)-1)*MOD_COM(cnt[3], 1)%MOD
        q = 0
        for i in range(2, cnt[3]+1):
            q += MOD_COM(cnt[3], i)
        q *= pow(2, n-cnt[3], MOD)
        ans -= p+q
        ans %= MOD
    if 0 < cnt[1] and 0 < cnt[2]:
        p = (pow(2, cnt[1], MOD)-1) * (pow(2, cnt[2], MOD)-1) % MOD
        p *= pow(2, cnt[0], MOD)
        L *= ((pow(2, cnt[1], MOD)-1) + (pow(2, cnt[2], MOD)-1) + 1) % MOD
        ans -= p
        ans %= MOD
    if 1 < cnt[0]:
        p = 0
        st = set()
        for v in dic.keys():
            if v in st:
                continue
            u = None
            if v[0] > 0 and v[1] > 0:
                u = (-1*v[1], v[0])
            else:
                u = (v[1], -1*v[0])
            x = dic[v]
            y = 0
            if u in dic:
                y = dic[u]
            cnt[0] -= x+y
            q = (pow(2, x, MOD)-1) * (pow(2, y, MOD)-1) * pow(2, cnt[0], MOD) * L % MOD
            p += q
            L *= ((pow(2, x, MOD)-1) + (pow(2, y, MOD)-1) + 1) % MOD
            L %= MOD
            p %= MOD
            st.add(v)
            st.add(u)
        p %= MOD
        ans -= p
        ans %= MOD
    print(ans%MOD)

if __name__ == "__main__":
    main()