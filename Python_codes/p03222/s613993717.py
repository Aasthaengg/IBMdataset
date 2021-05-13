import itertools

h, w, k = map(int, input().split())
mod = 10**9 + 7

# 縦棒を0-indexで考える
# dp[i][j] := 上から高さi(0,1,...,h)までの横棒を配置した時に、
#             0(問題文では1)からスタートしてjで終わるようなものの個数

dp = [[0 for _ in range(w)]for _ in range(h + 1)]
dp[0][0] = 1

# 縦線が1本の場合、以下の議論が成立しない
if w == 1:
    print(1)
    exit()

bridges = list(itertools.product([0, 1], repeat=w - 1))
# print(bridges)

for i in range(h):
    for bridge in bridges:

        # 橋が隣り合っていてはいけない
        tf = True
        for j in range(w - 2):
            if bridge[j] == 1 and bridge[j + 1] == 1:
                tf = False
                break
        if tf == False:
            continue

        for j in range(w):
            # 左端について
            if j == 0:
                # 橋がある時、右から流入
                if bridge[0] == 1:
                    dp[i + 1][j] += dp[i][j + 1]
                # 橋がない時、上から流入
                else:
                    dp[i + 1][j] += dp[i][j]

            # 右端について
            elif j == w - 1:
                # 橋がある時、左から流入
                if bridge[-1] == 1:
                    dp[i + 1][j] += dp[i][j - 1]
                # 橋がない時、上から流入
                else:
                    dp[i + 1][j] += dp[i][j]

            #　両端以外について
            else:
                # 両サイドに橋がない場合
                if bridge[j - 1] == 0 and bridge[j] == 0:
                    dp[i + 1][j] += dp[i][j]
                # 左だけ橋がある場合
                elif bridge[j - 1] == 1 and bridge[j] == 0:
                    dp[i + 1][j] += dp[i][j - 1]
                # 右だけ橋がある場合
                elif bridge[j - 1] == 0 and bridge[j] == 1:
                    dp[i + 1][j] += dp[i][j + 1]

            dp[i + 1][j] %= mod

print(dp[-1][k - 1])
