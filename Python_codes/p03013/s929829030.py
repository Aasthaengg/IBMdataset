import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, m = map(int, input().split())
    S = set(int(input()) for _ in range(m))

    a, b = 0, 1 # a[-1], a[0]
    for i in range(1, n + 1):
        if i in S:
            a, b = b, 0
        else:
            a, b = b, (a + b) % MOD

    print(b)
resolve()