# C_vacation
N = int( input() )
happiness = list()
for nn in range(N):
    h = [int(x) for x in input().split()]
    happiness.append( h )

dp = [[0]*3 for x in range(N)]
dp[0] = happiness[0]
for nn in range(1, N):
    for ii in range(3): # day nn's choice
        max_reward = 0
        for jj in range(3): # day (nn-1)'s choice
            r = dp[nn-1][jj] + happiness[nn][ii]
            if( ii != jj and r > max_reward ):
                max_reward = r
        dp[nn][ii] = max_reward

ans = 0
for ii in range(3):
    if( dp[-1][ii] > ans ):
        ans = dp[-1][ii]
print( ans )