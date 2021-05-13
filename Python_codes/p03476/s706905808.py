mx = 100005
q = int(input())

primes = [True for x in range(mx)]
primes[0] = False
primes[1] = False
for i in range(2, mx):
    if primes[i]:
        for j in range(i*i, mx, i):
            primes[j] = False

dp = [0 for x in range(mx)]
for i in range(1, mx):
    if i % 2 == 0:
        dp[i] = dp[i-1]
    else:
        if primes[i] and primes[(i+1)//2]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]

for i in range(q):
    l, r = map(int, input().split())
    print(dp[r] - dp[l-1])
    
