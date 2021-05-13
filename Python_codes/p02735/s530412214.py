
#ライブラリインポート
from collections import defaultdict

con = 10 ** 9 + 7
#入力受け取り
def getlist():
	return list(map(int, input().split()))
INF = float("inf")

#処理内容
def main():
	H, W = getlist()
	L = []
	for i in range(H):
		l = list(input())
		L.append(l)

	DP = [[INF] * W for i in range(H)]
	#初期化
	if L[0][0] == "#":
		DP[0][0] = 1
	else:
		DP[0][0] = 0

	for i in range(1, H):
		DP[i][0] = 0
	for i in range(1, W):
		DP[0][i] = 0

	for i in range(1, H):
		if L[i][0] != L[i - 1][0]:
			DP[i][0] += DP[i - 1][0] + 1
		else:
			DP[i][0] += DP[i - 1][0]

	for i in range(1, W):
		if L[0][i] != L[0][i - 1]:
			DP[0][i] += DP[0][i - 1] + 1
		else:
			DP[0][i] += DP[0][i - 1]

	for i in range(1, H):
		for j in range(1, W):
			if L[i][j] != L[i - 1][j]:
				DP[i][j] = min(DP[i][j], DP[i - 1][j] + 1)
			else:
				DP[i][j] = min(DP[i][j], DP[i - 1][j])

			if L[i][j] != L[i][j - 1]:
				DP[i][j] = min(DP[i][j], DP[i][j - 1] + 1)
			else:
				DP[i][j] = min(DP[i][j], DP[i][j - 1])

	# print(DP)

	ans = int((DP[-1][-1] + 1) // 2)
	print(ans)


if __name__ == '__main__':
	main()