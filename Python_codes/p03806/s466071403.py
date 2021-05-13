import sys
input = sys.stdin.buffer.readline
import numpy as np

def main():
    N,A,B = map(int,input().split())
    INF = 10**10
    dp = np.full((N+1,10*N+1,10*N+1),INF)
    dp[0][0][0] = 0
    
    for i in range(N):
        a,b,c = map(int,input().split())
        dp[i+1][a:,b:] = np.minimum(dp[i][a:,b:],dp[i][:10*N+1-a,:10*N+1-b]+c)
        dp[i+1] = np.minimum(dp[i],dp[i+1])
    
    ans = INF
    x,y = A,B
    while x < 10*N+1 and y < 10*N+1:
        ans = min(ans,dp[N][x][y])
        x += A
        y += B
        
    print(int(ans) if ans != INF else -1)

if __name__ == "__main__":
    main()
