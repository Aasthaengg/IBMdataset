N = int(input())
tannis = [1]

i = 1
while 6**i <= N:
    tannis.append(6**i)
    i += 1

i = 1
while 9**i <= N:
    tannis.append(9**i)
    i += 1

dp = [float('inf') for _ in range(N+1)]
dp[0] = 0

for i in range(1, N+1):
    for t in tannis:
        if i-t >= 0:
            dp[i] = min(dp[i], dp[i-t]+1)

#print(dp)
print(dp[N])
