#設定
import sys
input = sys.stdin.buffer.readline

#ライブラリインポート
from collections import defaultdict, deque

#入力受け取り
def getlist():
	return list(map(int, input().split()))

#処理内容
def main():
	#入力
	N = int(input())
	outE = defaultdict(list)
	inE = defaultdict(int)
	for i in range(N):
		A = getlist()
		for j in range(N - 2):
			a, b = sorted([A[j] - 1, i])
			c, d = sorted([A[j + 1] - 1, i])
			outE[a * N + b].append(c * N + d)
			inE[c * N + d] += 1

	#キュー初期化
	Q = []
	for i in range(N):
		for j in range(i + 1, N):
			if inE[i * N + j] == 0:
				Q.append(i * N + j)
	#print(Q)
	#計算
	judge = "Yes"
	cnt = 0
	ans = 1
	while True:
		q = []
		for i in Q:
			for j in outE[i]:
				inE[j] -= 1
				cnt += 1
				if inE[j] == 0:
					q.append(j)

		if q == []:
			break
		else:
			Q = q
		ans += 1
	# print(ans)
	# print(cnt)

	if cnt != N * (N - 2):
		print(-1)
	else:
		print(ans)

if __name__ == '__main__':
	main()