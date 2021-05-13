mod = 10 ** 9 + 7


def mod_pow(a, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        half_p = p // 2
        half = mod_pow(a, half_p)
        return half * half % mod
    else:
        return a * mod_pow(a, p - 1) % mod


def calc_comb(a, b):
    if b > a - b:
        return calc_comb(a, a - b)

    ans_mul = 1
    ans_div = 1
    for i in range(b):
        ans_mul *= (a - i)
        ans_div *= (i + 1)
        ans_mul %= mod
        ans_div %= mod

    ans = ans_mul * mod_pow(ans_div, mod - 2) % mod
    return ans


N, M = map(int, input().split())
ans = 1
rest = M
for i in range(2, int(M ** 0.5) + 1):
    if rest % i == 0:
        cnt = 0
        while rest % i == 0:
            cnt += 1
            rest = rest // i
        ans *= calc_comb(N + cnt - 1, N - 1)
        ans %= mod
if rest != 1:
    ans *= calc_comb(N + 1 - 1, N - 1)
    ans %= mod
print(ans)
