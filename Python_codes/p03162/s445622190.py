# 定数
A = 0
B = 1
C = 2

# リスト
N = int(input())
a = list()
b = list()
c = list()

dp = list()

for i in range (0, N):
	happiness = list(map(int, input().split()))
	a.append(happiness[A])
	b.append(happiness[B])
	c.append(happiness[C])

for i in range (0, N + 1):
	dp.append([0, 0, 0])


for i in range(1, N + 1):
	dp[i][A] = max(dp[i-1][B] + a[i-1], dp[i-1][C] + a[i-1])
	dp[i][B] = max(dp[i-1][A] + b[i-1], dp[i-1][C] + b[i-1])
	dp[i][C] = max(dp[i-1][A] + c[i-1], dp[i-1][B] + c[i-1])

# N+1日目の幸福度と考えると、添え字は N

print(max(dp[N][A], dp[N][B], dp[N][C]))