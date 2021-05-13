n,t = map(int,input().split())
ab = [[int(i) for i in input().split()] for j in range(n)]

dp = [[0 for i in range(t)] for j in range(n+1)]
ab.sort()

ans = 0

for i in range(n):
    for j in range(t):
        #for k in range(2):
        #dp[i+1][j] = max(dp[i][j],dp[i-1][j])
        dp[i+1][j] = dp[i][j]
        #print(j,ab[i][0])
        if j >= ab[i][0]:
        #if dp[i][j] < dp[i][j-ab[i][0]] + ab[i][1]:
        #    dp[i+1][j] = dp[i][j-ab[i][0]] + ab[i][1]
            dp[i+1][j] = max(dp[i][j],dp[i][j-ab[i][0]] + ab[i][1])
        #print(dp)
    #print(h,dp)

#print(ab)
#print(dp)


max_num = [0]*n

for i in reversed(range(n)):
    #print(i)
    if i == 0:
        break
    if max_num[i] < ab[i][1]:
        max_num[i-1] = ab[i][1]
    else:
        max_num[i-1] = max_num[i]

#print(max_num)
#print(ab[2272:2336])
#exit()

ans = 0
for i in range(n-1):
    #print(i)
    if ans < dp[i+1][t-1]+max_num[i]:
        ans = dp[i+1][t-1]+max_num[i]
        #print(i,ans,max_num[i],max_num[i+1],max_num[i-1])
    #ans = max(ans,)
    #print(max(ab[i:][1]))
    #print()
        
print(ans)
#print())