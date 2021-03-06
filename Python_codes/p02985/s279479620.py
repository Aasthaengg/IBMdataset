import sys

N,K = map(int,input().split())
E = [[] for _ in range(N)]
MOD = 10**9+7

for _ in range(N-1):
	u,v = map(int,input().split())
	u -= 1
	v -= 1
	E[u].append(v)
	E[v].append(u)

if N == 1:
	print(K)
	sys.exit()

color = [-1 for _ in range(N)]
dp = [-1 for _ in range(N)]

stack = []
color[u] = 1
ans = K
for i,v in enumerate(E[u]):
	stack.append(v)
	ans *= (K-i-1)
	ans %= MOD

while stack:
	u = stack.pop()
	color[u] = 1
	length = 0
	for v in E[u]:
		if color[v] == -1:
			stack.append(v)
			length += 1
	if dp[length] == -1:
		tmp = 1
		for i in range(K-1-length,K-1):
			tmp *= i
			tmp %= MOD
		ans *= tmp
		dp[length] = tmp
	else:
		ans *= dp[length]
	ans %= MOD

print(ans%MOD)