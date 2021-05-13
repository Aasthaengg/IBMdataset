from collections import defaultdict


def fraction(a, b):
    """a/b を既約分数 numer/denom として求める
    denom は必ず非負整数
    numer = denom = 0 のときは numer/denom = 0/0
    numer = 0 のときは numer/denom = 0/1
    denom = 0 のときは numer/denom = 1/0
    """
    numer, denom = a, b
    if numer == denom == 0:
        return 0, 0
    elif numer == 0:
        return 0, 1
    elif denom == 0:
        return 1, 0

    # GCD(a, b) を計算して約分する
    while b:
        a, b = b, a % b
    gcd_ab = a
    numer = numer // gcd_ab
    denom = denom // gcd_ab

    if denom < 0:  # denom は必ず非負整数
       numer, denom = -numer, -denom
    return numer, denom
  

n = int(input())
info = [list(map(int, input().split())) for i in range(n)]
MOD = 10 ** 9 + 7

memo = defaultdict(int)
for i in range(n):
    a, b = info[i]
    memo[fraction(a, b)] += 1

cnt_00 = 0
cnt_n0 = 0 
cnt_d0 = 0
ans = 1
used = set()
for frac in memo:
    numer, denom = frac
    if numer == 0 and denom == 0:
        cnt_00 += memo[frac]
        continue
    if frac in used:
        continue
    if numer == 0 or denom == 0:
        cnt1, cnt2 = 0, 0
        if (0, 1) in memo:
            cnt1 = memo[(0, 1)]
        if (1, 0) in memo:
            cnt2 = memo[(1, 0)]
        tmp = pow(2, cnt1, MOD) + pow(2, cnt2, MOD) - 1
        ans *= tmp
        used.add((0, 1))
        used.add((1, 0))
        continue

    rev_num, rev_den = -denom, numer
    if rev_den < 0:
        rev_num, rev_den = -rev_num, -rev_den

    cnt1 = memo[frac]
    cnt2 = 0
    if (rev_num, rev_den) in memo:
        cnt2 = memo[(rev_num, rev_den)]
    tmp = pow(2, cnt1, MOD) + pow(2, cnt2, MOD) - 1
    ans *= tmp
    ans %= MOD
    used.add((rev_num, rev_den))

ans = ans + cnt_00
print((ans - 1) % MOD)