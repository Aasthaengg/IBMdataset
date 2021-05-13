n = int(input())
k = int(input())
x = list(map(int,input().split()))

dp = [0 for i in range(n)]
for i in range(n):
    dp[i] = min( abs(x[i]-0) , abs(x[i]-k)) * 2

print(sum(dp))