n,m = map(int,input().split())
cost = []
key = []
inf = int(1e9)
for i in range(m):
    a,b = map(int,input().split())
    c = list(map(int,input().split()))
    cost.append(a)
    cnt = 0
    for j in range(1,n+1):
        if j in c:
           cnt += 2**(n-j)
    key.append(bin(cnt))
dp = [inf]*(2**n)
for i in range(m):
    dp[int(key[i],0)] = min(cost[i],dp[int(key[i],0)])
for i in range(2**n):
    if dp[i] != inf:
        for j in range(m):
            k = int(key[j], 0)
            tar = k | i
            dp[tar] = min(dp[tar], dp[i] + cost[j])
if dp[-1] == inf:
    print(-1)
else:
    print(dp[-1])



