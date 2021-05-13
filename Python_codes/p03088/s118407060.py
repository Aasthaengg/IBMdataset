import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    MOD = 10**9+7
    N = int(input())
    I, J, K, L = N, 4, 4, 4
    # dpテーブル dp[i][j][k][l]:=i文字目までで末尾3桁が'ijk'のものの個数であるとき作れる，長さiの文字列の個数
    dp = [[[[0]*(L+1) for _ in range(K+1)] for _ in range(J+1)]
          for _ in range(I+1)]
    # 初期条件
    dp[0][0][0][0] = 1
    # ループ
    for i in range(1, I+1):
        for j in range(J+1):
            for k in range(K+1):
                for l in range(L+1):
                    for a in range(1, 5):

                        if [k, l, a] == [1, 3, 2]:
                            continue
                        if [k, l, a] == [1, 2, 3]:
                            continue
                        if [k, l, a] == [2, 1, 3]:
                            continue
                        if [j, l, a] == [1, 2, 3]:
                            continue
                        if [j, k, a] == [1, 2, 3]:
                            continue

                        dp[i][k][l][a] += dp[i-1][j][k][l]

    ans = 0
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                ans += dp[I][j][k][l]

    print(ans % MOD)


resolve()