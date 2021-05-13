import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]

MOD = 10**9 + 7


def f(ls):
    n = len(ls)
    s = 0
    for i, x in enumerate(ls):
        s += (i + 1) * (n - i) * x
        s %= MOD
    return s


n, m = ril()
ls0 = ril()
ls1 = ril()
ls0 = [b - a for a, b in zip(ls0, ls0[1:])]
ls1 = [b - a for a, b in zip(ls1, ls1[1:])]
print(f(ls0) * f(ls1) % MOD)