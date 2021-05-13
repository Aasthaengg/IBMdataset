N,K = map(int,input().split())
A = list(map(int,input().split()))
x = 50
lst1 = [0]*x
lst0 = [0]*x
for i in range(x):
    for Ai in A:
        if Ai >> i & 1:
            lst1[i] += 1
        else:
            lst0[i] += 1
dp = [[0,0] for _ in range(x)] # dp[i][1]はK以下確定、dp[i][0]は非確定
dp[x-1][1] = -1
for i in range(x-1)[::-1]:
    if K >> i & 1:
        if dp[i+1][1] == -1:
            dp[i][1] = lst1[i]*(1 << i)
        else:
            dp[i][1] = max((dp[i+1][1]+lst0[i]*(1 << i)),dp[i+1][0]+lst1[i]*(1 << i))
        dp[i][0] = dp[i+1][0]+max(lst1[i],lst0[i])*(1 << i)
    else:
        if dp[i+1][1] == -1:
            dp[i][1] = -1
            dp[i][0] = dp[i+1][0]+lst1[i]*(1 << i)
        else:
            dp[i][1] = dp[i+1][1]+max(lst1[i],lst0[i])*(1 << i)
            dp[i][0] = max(dp[i+1][0]+lst1[i]*(1 << i),dp[i+1][1]+lst0[i]*(1 << i))
print(dp[0][0])