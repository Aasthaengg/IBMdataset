import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

def main():
    N = int(input())
    a = list(map(int,input().split()))
    active = []
    
    for i in range(N):
        active.append((a[i],i))
        
    active.sort(key=itemgetter(0),reverse=True)
    dp = [[0]*(N+1) for _ in range(N+1)]
    
    for i in range(N):
        for j in range(i+1):
            x,y = j,i-j
            dp[x+1][y] = max(dp[x+1][y],dp[x][y]+active[x+y][0]*(abs(active[x+y][1]-x)))
            dp[x][y+1] = max(dp[x][y+1],dp[x][y]+active[x+y][0]*(abs(active[x+y][1]-(N-y-1))))

    ans = 0
    for i in range(N+1):
        ans = max(ans,dp[i][N-i])
        
    print(ans)
    
if __name__ == "__main__":
    main()
