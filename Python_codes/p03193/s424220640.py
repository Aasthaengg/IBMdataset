import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, h, w = map(int, input().split())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += a >= h and b >= w
    print(ans)
resolve()