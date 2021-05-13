import sys
input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    V = N
    dp = []
    for i in range(N):
        dp.append(list(map(int,input().split())))
    edge = [[True]*N for _ in range(N)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                a = dp[i][j]
                b = dp[i][k]+dp[k][j]
                if a > b:
                    print(-1)
                    exit(0)
                elif a == b and k != i and k != j:
                    edge[i][j] = False
                    edge[j][i] = False
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if edge[i][j]:
                ans += dp[i][j]
    print(ans)