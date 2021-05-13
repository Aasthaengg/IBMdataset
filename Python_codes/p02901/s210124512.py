import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    n, m = map(int, input().split())
    key = []  # 集合S，コスト
    for i in range(m):
        a, b = map(int, input().split())
        s = 0
        C = list(map(int, input().split()))
        for j in range(b):
            C[j] -= 1
            s |= 1 << C[j]  # C[j]桁目のbitを1にする
        key.append((s, a))
    INF = 10**9+7
    dp = [INF]*(2**n)
    dp[0] = 0

    for s in range(2**n):
        for i in range(m):
            t = s | key[i][0]
            cost = dp[s]+key[i][1]
            dp[t] = min(dp[t], cost)

    print(dp[-1] if dp[-1] != INF else -1)


resolve()