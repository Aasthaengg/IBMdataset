from collections import Counter

S = input()
n = len(S)

dp = [0]*(n+1)

dp[n-1] = int(S[-1])

for i in range(n-2,-1,-1):
    dp[i] = (dp[i+1]+pow(10,n-i-1,2019)*int(S[i]))%2019

ans = Counter(dp)
cnt = 0
for i in ans.values():
    cnt += i*(i-1)//2
    
print(cnt)
