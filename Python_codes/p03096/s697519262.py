MOD = 10 ** 9 + 7
n = int(input())
c = [int(input()) for _ in range(n)]
d = [c[0]]
for i in range(1, n):
	if c[i] != d[-1]:
		d.append(c[i])
#print(d)
n = len(d)
rightmost = [-1] * 200001
seg = []
for i in range(n):
	if rightmost[d[i]] >= 0:
		seg.append([rightmost[d[i]], i])
	rightmost[d[i]] = i

#print(seg)
dp = [1 for _ in range(n)]
M = len(seg)
cnt = 0
for i in range(1, n):
	if cnt == M:
		dp[i] = dp[i-1]
	elif i == seg[cnt][1]:
		dp[i] = dp[i-1] + dp[seg[cnt][0]]
		cnt += 1
	else:
		dp[i] = dp[i-1]
	dp[i] %= MOD
print(dp[-1])