H, W, K = map(int, input().split())
mod = 10 ** 9 + 7
dp_H1 = [[0] * 2 for _ in range(W + 1)]
#dp_H1: H=1の縦棒をi本用意した時、できるあみだの組み合わせはdp_H1[i][0]+dp_H1[i][1]

dp_row_where = [[0] * (W + 2) for _ in range(H + 1)]
#dp_row_where[i][j]: i行目の時点で、j本目の縦棒に到達できる組み合わせ

dp_H1[0][0] = 1
dp_H1[1][0] = 1

for i in range(2, W + 1):
	dp_H1[i][0] = dp_H1[i - 1][0] + dp_H1[i - 1][1]
	dp_H1[i][0] %= mod
	dp_H1[i][1] = dp_H1[i - 1][0]
	dp_H1[i][1] %= mod

dp_row_where[0][1] = 1

for i in range(1, H + 1):
	for j in range(1, W + 1):
		#j番目の縦棒から真下に降りる場合
		dp_row_where[i][j] += dp_row_where[i - 1][j] * sum(dp_H1[j - 1]) * sum(dp_H1[W - j])
		#print(sum(dp_H1[j - 1]), sum(dp_H1[W - j]))
		#j-1番目の縦棒から到達する場合
		dp_row_where[i][j] += dp_row_where[i - 1][j - 1] * sum(dp_H1[j - 2]) * sum(dp_H1[W - j])
		
		#j+1番目の縦棒から到達する場合
		dp_row_where[i][j] += dp_row_where[i - 1][j + 1] * sum(dp_H1[j - 1]) * sum(dp_H1[W - j - 1])
		
		dp_row_where[i][j] %= mod
		
print(dp_row_where[H][K])
#print(dp_H1)
#print(dp_row_where)
