n,m = map(int,input().split())
c = list(map(int,input().split()))

dp = [None]*50001
for i in c:
    dp[i] = 1

for i in range(1,n+1):
    if dp[i]:
        continue
    min_count = float('inf')
    for j in c:
        if i-j>0:
            min_count = min(min_count,1+dp[i-j])
            
    dp[i] = min_count
    
print(dp[n])
