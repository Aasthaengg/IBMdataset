R, C, K = map(int, input().split())
item = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    item[r][c] = v

# 多次元配列を生成する際、使いたい引数を逆順で書くと上手くいく

# dp = [[[0 for _ in range(4)] for _ in range(C + 1)] for _ in range(R + 1)]
# とするとTLEだった。(R+1)*4(C+1)だと通るみたいだが、あまり本質的ではない気がする。
# 以下ではdp0,dp1,dp2,dp3という4つの配列を作ることにする。

dp0 = [[0 for _ in range(C + 1)]for _ in range(R + 1)]
dp1 = [[0 for _ in range(C + 1)]for _ in range(R + 1)]
dp2 = [[0 for _ in range(C + 1)]for _ in range(R + 1)]
dp3 = [[0 for _ in range(C + 1)]for _ in range(R + 1)]

for i in range(R + 1):
    for j in range(C + 1):
        # 何度も使うので変数に格納しておく
        # 以下を省略し、毎回配列を見に行く書き方をしたら少し遅くなった(400ms程度)
        now0 = dp0[i][j]
        now1 = dp1[i][j]
        now2 = dp2[i][j]
        now3 = dp3[i][j]

        # 下に移動する場合、アイテムの個数はリセットされる
        if i <= R - 1:
            # 移動先のアイテムを取らない場合
            dp0[i + 1][j] = max(dp0[i + 1][j],
                                now0,
                                now1,
                                now2,
                                now3)

            # 移動先のアイテムを取る場合
            dp1[i + 1][j] = max(dp1[i + 1][j],
                                now0 + item[i + 1][j],
                                now1 + item[i + 1][j],
                                now2 + item[i + 1][j],
                                now3 + item[i + 1][j])

        # 右に移動する場合、アイテムの個数は維持される
        if j <= C - 1:
            # 移動先のアイテムを取らない場合
            dp0[i][j + 1] = max(dp0[i][j + 1],
                                now0)
            dp1[i][j + 1] = max(dp1[i][j + 1],
                                now1)
            dp2[i][j + 1] = max(dp2[i][j + 1],
                                now2)
            dp3[i][j + 1] = max(dp3[i][j + 1],
                                now3)

            # 移動先のアイテムを取る場合
            dp1[i][j + 1] = max(dp1[i][j + 1],
                                now0 + item[i][j + 1])
            dp2[i][j + 1] = max(dp2[i][j + 1],
                                now1 + item[i][j + 1])
            dp3[i][j + 1] = max(dp3[i][j + 1],
                                now2 + item[i][j + 1])

# 最終的にR行で取るアイテムの個数についてそれぞれ調べる、3個が最適とは限らない
ans = max(dp0[-1][-1],
          dp1[-1][-1],
          dp2[-1][-1],
          dp3[-1][-1])

print(ans)
