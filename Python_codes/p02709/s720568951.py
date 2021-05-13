n=int(input())
a= list(map(int, input().split()))

# aの各要素とインデックスを紐付け
for i in range(n):
    a[i]=[a[i],i]
a.sort(reverse=True)

# dp[i][l]:大きいものからi個位置決めてそのうち左がl（右がi-l）の時のMAX
dp=[[0]*(n+1) for i in range(n+1)]

for i in range(n):
    for j in range(i+1):
        # i番目を左に置く時、左に一つズレる
        dp[i+1][j+1]=dp[i][j]+abs(a[i][1]-j)*a[i][0]
    for j in range(i+1):
        # i番目を右に置く時
        dp[i+1][j]=max(dp[i+1][j],dp[i][j]+abs(a[i][1]-(n-1-(i-j)))*a[i][0])

print(max(dp[-1]))
