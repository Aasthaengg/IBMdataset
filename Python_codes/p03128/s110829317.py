import sys
input = sys.stdin.readline
'''
allinputs = iter(input().splitlines())
input = lambda : next(allinputs)
#'''
N, M = map(int, input().split())
A = list(map(int, input().split()))

recipe = [2, 5, 5, 4, 5, 6, 3, 7, 6]
available =[]
dp = [-1] * (N + 1)

for i in range(M):
	available.append((A[i], recipe[A[i] - 1]))
	
available.sort(reverse = True)
dp[0] = 0

for i in range(1, N + 1):
	for j in range(M):
		k = i - available[j][1]
		if k >= 0 and dp[k] >= 0:
			if dp[k] + 1 > dp[i]:
				dp[i] = dp[k] + 1

cost = 0
ans = ''

for i in range(dp[N]):
	for j in range(M):
		if N - cost - available[j][1] >= 0 and dp[N - cost - available[j][1]] == dp[N - cost] - 1:
			cost += available[j][1]
			ans += str(available[j][0])
			break
	
print(ans)