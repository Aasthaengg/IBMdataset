import sys
import numpy as np
# from numba import njit

# 公式解説を見てからやった
# 複数サイクルでき、1-K回移動可能
# N < 5000?多分、O(N * 2N)くらいで行けそうに見えるが。。。

# @njit(cache=False)
def main(N,K,P,C): #,ans):


	# XeXは、Float?
	# numbaの場合、intでないとまずいのかもしれないので、そのまま1e9はヤバそう
	# ans = -1e9
	ans = int(-1e9)		
	# ans = -10 ** 9		# これはOK

	# 一度計算したサイクル情報を一応キャッシュしておく。。。
	# あんまり意味なさそう
	cycleIDs = np.full( N, -1, dtype=np.int64 )
	cycleInfs = []


	# print(P)

	cycleID = 0

	for n in range(N):

		v = n
		currentCycleItemCnt = 0
		currentCycleTotal = 0

		if cycleIDs[v] != -1:
			currentCycleItemCnt, currentCycleTotal = cycleInfs[ cycleIDs[v] ]
			# print(currentCycleItemCnt, currentCycleTotal)
		else:
			while True:
				# 全頂点について、属するサイクルを計算する
				currentCycleItemCnt += 1
				currentCycleTotal += C[v]

				v = P[v]
				if v == n:
					# サイクル発見
					cycleInfs.append( (currentCycleItemCnt, currentCycleTotal) )
					cycleID += 1
					break

				# 一応、一度サイクルを計算した頂点については、
				# その頂点の属するサイクルの情報をメモっておく。。。
				cycleIDs[v] = cycleID

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
				cycleLoopCnt = int(( K - procCnt ) // currentCycleItemCnt)

			# print("v=", v, "currentCycleSumTmp=", currentCycleSumTmp, procCnt)
			tmp = currentCycleSumTmp + cycleLoopCnt * currentCycleTotal
			ans = max( int(ans), int(tmp) )

			v = P[v]
			if v == n:
				# サイクル終了
				break

	print(int(ans))

if sys.argv[-1]=='ONLINE_JUDGE':
	# from numba import njit
	from numba.pycc import CC
	cc=CC('my_module')
	cc.export('main','void(i8,i8,i8[:],i8[:])')(main)
	# main=njit(main, cache=True)
	cc.compile()
	exit(0)
from my_module import main



if __name__ == "__main__":
	N,K = map(int,input().split())
	P = np.array( input().split(), np.int64 )
	P -= 1
	C = np.array( input().split(), np.int64 )

	main(N,K,P,C) #,ans)
	#print(ans)


