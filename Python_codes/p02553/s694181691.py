import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    a, b, c, d = map(int, input().split())
    print(max(a * c, a * d, b * c, b * d))
resolve()