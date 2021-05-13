import sys
sys.setrecursionlimit(2147483647)
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n, p = map(int, input().split())
    S = input()

    if p == 2 or p == 5:
        res = 0
        for i, c in enumerate(S, 1):
            if int(c) % p == 0:
                res += i
        print(res)
        return

    res = 0
    now = 0
    counter = Counter()
    counter[0] = 1
    for i in range(n):
        now = (10 * now + int(S[i])) % p
        k = now * pow(10, (p - 2) * i, p) % p
        res += counter[k]
        counter[k] += 1
    print(res)
resolve()