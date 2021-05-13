import sys


def resolve():
    readline = sys.stdin.readline    # 1行だけ文字列にする

    N = int(readline())
    H = [int(x) for x in readline().split()]

    # DP配列全体を「DPの種類に応じた初期値」で初期化
    dp = [0] * N
    
    # 初期条件を入力
    dp[0] = 0
    dp[1] = dp[0] + abs(H[1] - H[0])

    # ループを回す
    for i in range(2, N):
        dp[i] = min(dp[i - 1] + abs(H[i] - H[i - 1]),
                    dp[i - 2] + abs(H[i] - H[i - 2]))
    
    # テーブルから解を得て出力
    print(dp[-1])


resolve()