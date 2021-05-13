import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input())
    print("YES" if abs(b - a) <= t * (v - w) else "NO")
resolve()