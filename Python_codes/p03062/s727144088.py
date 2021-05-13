## https://atcoder.jp/contests/abc125/tasks/abc125_d

N = int(input())
N_List = list(map(int,input().split()))

dp = [[0] * 2 for i in range(N)]

dp[1][False] = N_List[0] + N_List[1]
dp[1][True] = (N_List[0] + N_List[1])*(-1)

for i in range(2,N):
    dp[i][False] = max(dp[i-1][True] + N_List[i],dp[i-1][False] + N_List[i])
    dp[i][True] = max(dp[i-1][True] + N_List[i-1]*2 + N_List[i]*(-1) ,
                      dp[i-1][False] + N_List[i-1]*(-2) + N_List[i]*(-1))

print(max(dp[N-1]))