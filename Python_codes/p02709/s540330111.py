n = int(input())
a = list(map(int,input().split()))

# 移動先xi
# p[i] = a[i]*|i-xi|
# if i > xi:ans = sum(p[i]) = sum(a[i]*(i-xi)) -> a[i]の大きい順にxiを小さくする
# if i < xi:ans = sum(p[i]) = sum(a[i]*(xi-i)) -> a[i]の小さい順にxiを小さくする
# dp[i][j]:i人がi-xi（左にいく）,j人がxi-i（右にいく）で計算（i*xi = j*xi)

A=[]
for i in range(n):
    A.append((a[i],i))
A.sort(key = lambda x:x[0], reverse=True)
dp = [[-float("inf")]*(n+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(n):
    a,w = A[i]
    for x in range(n+1):
        y = i-x+1
        if x>0:
            dp[i+1][x]=max(dp[i+1][x],dp[i][x-1]+a*abs(w-(x-1)))
        if y>=0:
            dp[i+1][x]=max(dp[i+1][x],dp[i][x]+a*abs(w-(n-y)))

print(max(dp[n]))