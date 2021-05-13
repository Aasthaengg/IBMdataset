n = int(input())
l = list(map(int,input().split()))
dp = []
dp.append(0)
dp.append(abs(l[1]-l[0]))
for i in range(2,n):
    dp.append(0)
for i in range(2,n):
    m = min(dp[i-2]+abs(l[i-2]-l[i]),dp[i-1]+abs(l[i-1]-l[i]))
    dp[i] = m
print(dp[n-1])