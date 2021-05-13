MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    n,m = map(int,input().split())
    s = list(map(int,input().split()))
    t = list(map(int,input().split()))
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    if s[0] == t[0]:
        dp[1][1] = 1
    else:
        dp[1][1] = 0
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                continue
            if s[i] == t[j]:
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] + 1)%MOD
            else:
                dp[i + 1][j + 1] = (dp[i][j + 1] + dp[i + 1][j] - dp[i][j])%MOD
    print((dp[-1][-1] + 1)%MOD)

if __name__ =='__main__':
    main()   
