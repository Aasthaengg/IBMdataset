
H,W,M=map(int,input().split())

HSum=[0 for _ in range(H)]
WSum=[0 for _ in range(W)]


bombs = set()
for _ in range(M):
	hi,wi = map(lambda x:int(x)-1,input().split())
	HSum[hi] += 1
	WSum[wi] += 1
	bombs.add( (hi,wi) )
# print(HSum)
# print(WSum)



curMax = 0

## 計算量多すぎ。。
# for h in range(H):
# 	for w in range(W):
# 		tmp = HSum[h] + WSum[w]
# 		if curMax <= tmp:
# 			if (h,w) in bombs:
# 				tmp -= 1
# 			curMax = max( curMax, tmp )

hMax = max(HSum)
wMax = max(WSum)
tmpMax = hMax + wMax

ans = 0

hSumMaxOnly = [h for h, x in enumerate(HSum) if x == hMax]
wSumMaxOnly = [w for w, y in enumerate(WSum) if y == wMax]

for h in hSumMaxOnly:
	if ans == tmpMax:
		break
	for w in wSumMaxOnly:
		if (h,w) in bombs:
			ans = tmpMax - 1
		else:
			ans = tmpMax
			break



print(ans)
