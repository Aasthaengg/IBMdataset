n = int(input())

m = [[0 for _ in range(n+1)] for _ in range(n+1)]
#mm = [[] for _ in range(n+1)]

for _ in range(n):
	tmp = [int(x) for x in input().split()]
	u,k,l = tmp[0],tmp[1],tmp[2:]
	#mm[u] += tmp[2:]
	for x in l:
		m[u][x] = 1
		
dp = [float('inf') for _ in range(n+1)]
dp[1] = 0
queue = [1]

while queue:
	t = queue.pop(0)
	for i,x in enumerate(m[t]):
		if x == 1:
			if dp[i] > dp[t] + 1:
				dp[i] = dp[t] + 1
				queue.append(i)
			else:
				pass
		else:
			pass
			
for i,x in enumerate(dp):
	if i == 0:
		pass
	else:
		if x == float('inf'):
			print(i, -1)
		else:
			print(i, x)
			

	
