import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    a, b, c = map(int, input().split())
    if ~a&1 or ~b&1 or ~c&1:
        print(0)
    else:
        print(min(a * b, b * c, c * a))
resolve()