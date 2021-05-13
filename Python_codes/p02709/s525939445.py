N = int(input())
D = []
for i, a in enumerate(map(int, input().split())):
    D.append((a<<11) + i)
D.sort(reverse=True)
dp = [0]*(N+1)
for i, d in enumerate(D,start=1):
    x, a = d%(1<<11),d>>11
    for j in reversed(range(0, i+1)):
        res1 = dp[j-1]+a*(x-(j-1))*(j-1>=0)
        res2 = dp[j]+a*(N-(i-j)-x)*(j<=i-1)
        if res1>=res2: dp[j] = res1
        else: dp[j] = res2
print(max(dp))