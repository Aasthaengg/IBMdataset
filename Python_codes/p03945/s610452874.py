s = input()
n = len(s)

dp = [0]*n
dp[0]=1
for i in range(1,n):
    if s[i-1]==s[i]:
        continue
    dp[i]=1
print(sum(dp)-1)