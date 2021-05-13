
from collections import defaultdict
from math import gcd

def resolve():
    MOD = 1000000007

    N = int(input())
    dic = defaultdict(int)
    zeros = 0
    for _ in range(N):
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            zeros += 1
        else:
            g = gcd(a, b)
            a //= g
            b //= g
            if a < 0:
                a *= -1
                b *= -1
            if a == 0 and b == -1:
                b = 1
            dic[(a, b)] += 1

    ans = 1
    free = 0
    for (a, b), n in dic.items():
        if b > 0:
            if (b, -a) in dic:
                m = dic[(b, -a)]
                ans = ans * (pow(2, n, MOD) + pow(2, m, MOD) - 1) % MOD
            else:
                free += n
        else:
            if (-b, a) not in dic:
                free += n
                
    ans = (ans * pow(2, free, MOD) + zeros - 1) % MOD
    print(ans)

if __name__ == "__main__":
    resolve()