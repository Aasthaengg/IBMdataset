N = int(input())

a_list = []
b_list = []
c_list = []
for i in range(N):
    a, b, c = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    c_list.append(c)

dp = [[0]*3 for i in range(N)]
dp[0][0] = a_list[0]
dp[0][1] = b_list[0]
dp[0][2] = c_list[0]

for i in range(1,N):
    dp[i][0] = max(dp[i-1][1]+a_list[i], dp[i-1][2]+a_list[i])
    dp[i][1] = max(dp[i-1][0]+b_list[i], dp[i-1][2]+b_list[i])
    dp[i][2] = max(dp[i-1][0]+c_list[i], dp[i-1][1]+c_list[i])

ans = max(dp[N-1])
print(ans)