n,m = map(int,input().split())
a = [int(input()) for i in range(m)]
a.append(1000000)
dp = [0]*(n+1)
dp[0] = 1
j = 0
if a[j] == 1:
    j += 1
else:
    dp[1] = 1

for i in range(2,n+1):
    if i == a[j]:
        j += 1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
#print(dp)
print(dp[n])