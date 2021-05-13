n = int(input())
l = [1]
c = 1
while(6**c <= 100000):
    l.append(6**c)
    c += 1
c = 1
while(9**c <= 100000):
    l.append(9**c)
    c += 1
l.sort()
dp = [100001 for _ in range(n+1)]
dp[0] = 0
for i in range(len(l)):
    for j in range(l[i],n+1):
        dp[j] = min(dp[j],dp[j - l[i]]+1)
print(dp[n])