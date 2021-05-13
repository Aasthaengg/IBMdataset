import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(n - k):
        print("YNeos"[1 - (A[i + k] > A[i])::2])
resolve()