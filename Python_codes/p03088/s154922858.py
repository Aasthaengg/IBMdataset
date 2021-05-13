import sys; input = sys.stdin.buffer.readline
from collections import defaultdict
con = 10 ** 9 + 7; INF = float("inf")

def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	N = int(input())
	#A:0 G:1 C:2 T:3
	DP = [[0] * 64 for i in range(N)]
	for i in range(64):
		DP[2][i] = 1
	DP[2][6] = 0
	DP[2][9] = 0
	DP[2][18] = 0

	for p in range(2, N - 1):
		for i in range(4):
			for j in range(4):
				for k in range(4):
					for s in range(4):
						if not ((i == 0 and k == 1 and s == 2) or (i == 0 and j == 1 and s == 2)):
							DP[p + 1][16 * j + 4 * k + s] += DP[p][16 * i + 4 * j + k]
							DP[p + 1][16 * j + 4 * k + s] %= con

		DP[p + 1][6] = 0
		DP[p + 1][9] = 0
		DP[p + 1][18] = 0

	ans = sum(DP[N - 1])
	print(ans % con)


if __name__ == '__main__':
	main()