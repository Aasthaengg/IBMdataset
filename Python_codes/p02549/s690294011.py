N, K = map(int, input().split())
MOD = 998244353

lr = []
for _ in range(K):
    l, r = map(int, input().split())
    lr.append((l, r))
lr.sort()

dp = [0]*(N+1)
dpsum = [0]*(N+1)
dp[1] = 1
dpsum[1] = 1

# 区間の合計を複数回求める＝累積和
# 累積和を作りながらDPをする
for i in range(2, N+1):
    # マスiに移動できる数を求める
    for l, r in lr:
        # iの左側からiへ移動できる区間を求めるので、
        # lとrは逆になる
        li = max(i-r, 1)
        ri = i-l

        # 右のマスが0以下なら移動できないので次へ
        if ri < 1:
            continue

        dp[i] += dpsum[ri]-dpsum[li-1]
        dp[i] %= MOD
    dpsum[i] = dpsum[i-1]+dp[i]
print(dp[N])
