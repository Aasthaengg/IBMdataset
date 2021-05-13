import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
dest = [[] for _ in range(n)]
comein = [0 for _ in range(n)]
ro = [True for _ in range(n)]
dp = [0 for _ in range(n)]
for _ in range(m):
	x, y = map(int, input().split())
	dest[x-1].append(y-1)
	comein[y-1] += 1
	ro[y-1] = False

def search(leaf):
	global dp
	for i in dest[leaf]:
		comein[i] -= 1
		dp[i] = max(dp[i], dp[leaf] + 1)
		if comein[i] == 0:
			search(i)
	return

for j in range(n):
	if ro[j] == True:
		search(j)

print(max(dp))