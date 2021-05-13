import sys

def main():
    INF = -2**60
    N, M = map(int, sys.stdin.buffer.readline().split())
    XYZ = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]

    sgn = [[1,1,1], [1,1,-1],[1,-1,1],[1,-1,-1],[-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
    ans = INF 
    for a, b, c in sgn:
        dp = [INF]*(M+1)
        dp[0] = 0
        for x, y, z in XYZ:
            for j in range(M-1, -1, -1):
                if dp[j] == INF: continue
                s = dp[j]+ a*x + b*y + c*z
                if s > dp[j+1]:
                    dp[j+1] = s
        if dp[M] > ans:
            ans = dp[M]
    print(ans)

main()
