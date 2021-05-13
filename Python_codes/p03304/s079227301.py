import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, m, d = map(int, input().split())
    if d == 0:
        print((m - 1) / n)
    else:
        print(2 * (m - 1) * (n - d) / (n * n))
resolve()