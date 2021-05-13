# 公式解説を見てからやった
# 複数サイクルでき、1-K回移動可能
# N < 5000?多分、O(N * 2N)くらいで行けそうに見えるが。。。

if __name__ == "__main__":

	N,K = map(int,input().split())
	P = [ int(p)-1 for p in input().split() ]
	C = list(map(int,input().split()))

	# print(P)

	ans = -1e10

	for n in range(N):

		v = n
		currentCycleItemCnt = 0
		currentCycleTotal = 0

		while True:
			# 全頂点について、属するサイクルを計算する
			currentCycleItemCnt += 1
			currentCycleTotal += C[v]

			v = P[v]
			if v == n:
				# サイクル発見
				break

		procCnt = 0
		currentCycleSumTmp = 0

		while True:

			# 頂点vにコマが置かれた時の最高スコアを計算し、
			# これまでの最高スコアを上回ったら、これまでの最高スコアを更新する
			procCnt += 1
			currentCycleSumTmp += C[v]
			if K < procCnt:
				break

			cycleLoopCnt = 0
			if procCnt < K and 0 < currentCycleTotal:
				cycleLoopCnt = ( K - procCnt ) // currentCycleItemCnt

			# print("v=", v, "currentCycleSumTmp=", currentCycleSumTmp, procCnt)
			tmp = currentCycleSumTmp + cycleLoopCnt * currentCycleTotal
			ans = max( ans, tmp )

			v = P[v]
			if v == n:
				# サイクル終了
				break

	print(ans)
