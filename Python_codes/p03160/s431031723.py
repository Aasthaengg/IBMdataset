def cmin(a,b):
    if a>b:
        return b
    else:
        return a
 
N = int(input())
h = list(map(int,input().split()))
 
dp = [0] + [float("inf")]*(N-1)
dp[1]=abs(h[1]-h[0])
for i in range(2,N):
    dp[i] = cmin(dp[i-2]+abs(h[i]-h[i-2]),dp[i-1]+abs(h[i]-h[i-1]))
print(dp[-1])