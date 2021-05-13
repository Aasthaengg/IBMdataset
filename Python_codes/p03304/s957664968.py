import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, m, d = map(int, input().split())
    ans = (m - 1) / n
    if d > 0 and 2 * d + 1 <= n:
        ans *= 1 + (n - 2 * d) / n
    print(ans) 
resolve()