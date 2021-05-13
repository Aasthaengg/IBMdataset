H, W, K = map(int, input().split())
dp = [[]]
for i in range(0, W):
	dp[0].append(0)
dp[0][0] = 1
for i in range(0, H):
	next = []
	for j in range(0, W):
		next.append(0)
	for j in range(0, 2**(W-1)):
		lst = []
		m = j
		for k in range(0, W-1):
			lst.append(m%2)
			m //= 2
		flag = True
		for k in range(0, W-2):
			if lst[k] == 1 and lst[k+1] == 1:
				flag = False
				break
		if flag:
			notswapped = []
			for k in range(0, W):
				notswapped.append(True)
			for k in range(0, W-1):
				if lst[k] == 1:
					next[k+1] += dp[-1][k]
					next[k] += dp[-1][k+1]
					notswapped[k] = False
					notswapped[k+1] = False
			for k in range(0, W):
				if notswapped[k]:
					next[k] += dp[-1][k]
	dp.append(next)
print(dp[H][K-1]%(10**9+7))