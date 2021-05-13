import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():

    needs = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())), reverse=True)

    dp = [-1]*(N+1)
    # 初期条件
    dp[0] = 0

    # ループ
    for a in A:
        na = needs[a-1]
        for i in range(N+1):
            if i-na >= 0:
                if dp[i-na] == -1:
                    continue
                dp[i] = max(dp[i], dp[i-na]*10+a)

    print(dp[N])


resolve()