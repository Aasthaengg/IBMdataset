import sys
import numpy as np
# from numba import njit

# @njit(cache=True)
def calcCycle(N,K,P,C,cycleIDs,cycleItemCnts,cycleTotalScores):
	cycleID = 0

	for n in range(N):

		v = n
		currentCycleItemCnt = 0
		currentCycleTotal = 0

		if cycleIDs[v] != -1:
			continue
			# print(currentCycleItemCnt, currentCycleTotal)
		else:
			while True:
				# 全頂点について、属するサイクルを計算する
				currentCycleItemCnt += 1
				currentCycleTotal += C[v]

				v = P[v]
				if v == n:
					# サイクル発見
					cycleIDs[v] = cycleID
					cycleItemCnts[cycleID] = currentCycleItemCnt
					cycleTotalScores[cycleID] = currentCycleTotal
					cycleID += 1
					break

				# 一応、一度サイクルを計算した頂点については、
				# その頂点の属するサイクルの情報をメモっておく。。。
				cycleIDs[v] = cycleID

def upd(P,C,K,v,ans,currentCycleItemCnt,currentCycleTotal):

	# procCnt = 0
	currentCycleSumTmp = 0

	for k in range(min(K,currentCycleItemCnt)):

		# 頂点vにコマが置かれた時の最高スコアを計算し、
		# これまでの最高スコアを上回ったら、これまでの最高スコアを更新する

		procCnt = k+1
		currentCycleSumTmp += C[v]

		cycleLoopCnt = 0
		if 0 < currentCycleTotal:
			cycleLoopCnt = ( K - procCnt ) // currentCycleItemCnt

		# print("v=", v, "currentCycleSumTmp=", currentCycleSumTmp, "procCnt, cycleLoopCnt, currentCycleTotal=", procCnt, cycleLoopCnt, currentCycleTotal)
		ans = max( ans, currentCycleSumTmp + cycleLoopCnt * currentCycleTotal )
		v = P[v]

	return ans





def main(ans,N,K,P,C,cycleIDs,cycleItemCnts,cycleTotalScores):

	for n in range(N):

		v = n
		currentCycleItemCnt, currentCycleTotal = cycleItemCnts[ cycleIDs[v] ], cycleTotalScores[ cycleIDs[v] ]

		# ans=upd(P,C,K,v,ans,currentCycleItemCnt,currentCycleTotal)
		currentCycleSumTmp = 0
		for k in range(min(K,currentCycleItemCnt)):

			procCnt = k+1
			currentCycleSumTmp += C[v]

			cycleLoopCnt = 0
			if 0 < currentCycleTotal:
				cycleLoopCnt = ( K - procCnt ) // currentCycleItemCnt

			# print("v=", v, "currentCycleSumTmp=", currentCycleSumTmp, "procCnt, cycleLoopCnt, currentCycleTotal=", procCnt, cycleLoopCnt, currentCycleTotal)
			ans = max( ans, currentCycleSumTmp + cycleLoopCnt * currentCycleTotal )
			v = P[v]


	print(int(ans))

if sys.argv[-1]=='ONLINE_JUDGE':
	# from numba import njit
	from numba.pycc import CC
	cc=CC('my_module')
	cc.export('calcCycle','void(i8,i8,i8[:],i8[:],i8[:],i8[:],i8[:])')(calcCycle)
	cc.export('main','void(i8,i8,i8,i8[:],i8[:],i8[:],i8[:],i8[:])')(main)
	# cc.export('upd','i8(i8[:],i8[:],i8,i8,i8,i8,i8)')(upd)
	# cc.export('upd','UniTuple(i8,3)(i8[:],i8[:],i8,i8,i8,i8,i8)')(upd)
	# main=njit(main, cache=True)
	cc.compile()
	exit(0)
# from my_module import upd,calcCycle
from my_module import main,calcCycle
# from my_module import calcCycle



if __name__ == "__main__":
	N,K = map(int,input().split())
	P = np.array( input().split(), np.int64 )
	P -= 1
	C = np.array( input().split(), np.int64 )

	# 一度計算したサイクル情報を一応キャッシュしておく。。。
	# あんまり意味なさそう
	cycleIDs = np.full( N, -1, dtype=np.int64 )
	cycleItemCnts = np.full( N, -1, dtype=np.int64 )
	cycleTotalScores = np.full( N, -1, dtype=np.int64 )

	calcCycle(N,K,P,C,cycleIDs,cycleItemCnts,cycleTotalScores)

	# print(cycleItemCnts)

	ans = -1e18
	main(ans,N,K,P,C,cycleIDs,cycleItemCnts,cycleTotalScores)
	#print(ans)


