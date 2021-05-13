n = int(raw_input())
primes = [True] * ((10 ** 5) + 1)
for t in range(2,len(primes)):
	if primes[t]:
		k = 2
		while(k*t < len(primes)):
			primes[k*t] = False
			k +=1
dp = [0] * ((10 ** 5) + 1)
count = 0

for i in range(2,len(primes)):
	if primes[i] and primes[(i+1)/2] and i % 2:
		count +=1
	dp[i] = count
for _ in range(n):
	u,v = map(int, raw_input().split())
	print dp[v] - dp[u-1]