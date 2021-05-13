import sys
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = pow(10, 9) + 7
def powmod(m, p):
    if p == 0:
        return 1
    tmp = powmod(m, p // 2)
    if p & 1:
        return (tmp * tmp % MOD) * m % MOD
    else:
        return tmp * tmp % MOD


def main():
    n, m = map(int, input().split())
    div = defaultdict(lambda : 0)
    i = 2
    while i * i <= m:
        while m % i == 0:
            m //= i
            div[i] += 1
        i += 1
    if m > 1:
        div[m] += 1

    ans = 1
    for k, v in div.items():
        cn = v + n - 1
        v = min(v, cn - v)
        for i in range(v):
            ans *= cn - i
            ans %= MOD
        
        for i in range(2, v + 1):
            ans *= powmod(i, MOD - 2)
            ans %= MOD
    
    print(ans)


if __name__ == '__main__':
    main()
