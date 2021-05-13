n = int(input())

felicidade = []

for x in range(n):
    felicidade.append(list(map(int,input().split())))

dp = []

dp.append([felicidade[0][0],felicidade[0][1],felicidade[0][2]])

for i in range(n-1):
    dp.append([0,0,0])


for dia in range(1,n):
    dp[dia][0] = felicidade[dia][0] + max(dp[dia-1][1], dp[dia-1][2])
    dp[dia][1] = felicidade[dia][1] + max(dp[dia-1][0],dp[dia-1][2])
    dp[dia][2] = felicidade[dia][2] + max(dp[dia-1][0], dp[dia-1][1])


print(max(dp[n-1]))
