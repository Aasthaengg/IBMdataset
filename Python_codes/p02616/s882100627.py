import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
mul = lambda x, y : x * y % MOD
from functools import reduce
def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(key = abs, reverse = 1)

    if all(a < 0 for a in A) or n == k:
        if k & 1:
            print(reduce(mul, A[-k:]))
        else:
            print(reduce(mul, A[:k]))
        return

    pos = []
    neg = []
    for a in A:
        if a >= 0:
            pos.append(a)
        else:
            neg.append(-a)

    pos.reverse()
    neg.reverse()
    ans = 1
    if k & 1:
        ans *= pos.pop()
        k -= 1

    for _ in range(k // 2):
        if len(pos) >= 2 and len(neg) >= 2:
            a, b = pos[-2:]
            c, d = neg[-2:]
            if a * b >= c * d:
                ans *= pos.pop()
                ans *= pos.pop()
                ans %= MOD
            else:
                ans *= neg.pop()
                ans *= neg.pop()
                ans %= MOD
        elif len(pos) >= 2:
            ans *= pos.pop()
            ans *= pos.pop()
            ans %= MOD
        elif len(neg) >= 2:
            ans *= neg.pop()
            ans *= neg.pop()
            ans %= MOD
    print(ans)
resolve()