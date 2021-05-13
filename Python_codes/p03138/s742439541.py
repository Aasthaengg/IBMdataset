#参照　https://atcoder.jp/contests/abc117/submissions/7661660

import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())

A = list(map(int, input().split()))

# dp[桁数][0 or 1] 
# 0: Kより小さいことが未確定
# 1: Kより小さいことが確定
dp = [[-1 for _ in range(2)] for _ in range(55)]
dp[0][0] = 0

for d in range(50):
    mask = 1 << (50 - d - 1)

    # A で元々d桁目にビットが立っている個数
    num = 0
    for i in range(N):
        if A[i] & mask:
            num += 1

    # Xのd桁目をに0した時の増加分
    add0 = mask * num
    # Xのd桁目をに1した時の増加分
    add1 = mask * (N - num)

    # 1 => 1への遷移
    if dp[d][1] != -1:
        dp[d+1][1] = max(dp[d+1][1], dp[d][1] + max(add0, add1))

    # 0 => 1への遷移
    # Kのd桁目が1の時、Xのd桁目を0にする場合    
    if dp[d][0] != -1:
        if K & mask:
            dp[d+1][1] = max(dp[d+1][1], dp[d][0] + add0)

    # 0 => 0への遷移
    # Kのd桁目が1の時、Xのd桁目を1
    # Kのd桁目が0の時、Xのd桁目を0にする場合
    if dp[d][0] != -1:
        if K & mask:
            dp[d+1][0] = max(dp[d+1][0], dp[d][0] + add1)
        else:
            dp[d+1][0] = max(dp[d+1][0], dp[d][0] + add0)

print(max(dp[50][0], dp[50][1]))