import sys
sys.setrecursionlimit(2147483647)
INF = float("inf")
MOD = 10**9 + 7 # 998244353
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (k + 1)

    for i in range(k + 1):
        if dp[i]:
            continue
        for a in A:
            if i + a <= k:
                dp[i + a] = True

    print("First" if dp[k] else "Second")
resolve()