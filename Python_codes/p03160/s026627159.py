from sys import stdin
n = int(stdin.readline())
h = list(map(int,stdin.readline().split()))
dp = [0]
for i in range(1,n):
    dp.append(min(dp[i-1]+abs(h[i]-h[i-1]),10**9 if i==1 else dp[i-2]+abs(h[i]-h[i-2])))
print(dp[-1])