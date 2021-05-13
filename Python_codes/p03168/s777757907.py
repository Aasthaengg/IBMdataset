import numpy as np

if __name__=='__main__':
    N = int(input())
    p = np.array(list(map(float,input().split())))
    
    dp = np.zeros([N+1,N+1],dtype=float)
    dp[0][0] = 1.0
    
    for i,p in enumerate(p):
        dp[i+1][:] = dp[i][:]*(1-p)
        dp[i+1][1:] += dp[i][:-1]*p
    
    
    ans = N//2 + 1
    print(dp[N][ans:].sum())