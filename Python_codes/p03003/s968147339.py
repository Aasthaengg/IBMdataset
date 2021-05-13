#editorial参照
#そもそもの漸化式
#2次元累積和
#dp累積和のdpを含む漸化式 & dp消せる
n,m = map(int, input().split( ))

s = list(map(int, input().split( )))
t = list(map(int, input().split( )))

mod = 10**9 + 7

dp_sum = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp_sum[i][j] = dp_sum[i-1][j] + dp_sum[i][j-1] + 1
            dp_sum[i][j] %= mod
        else:
            dp_sum[i][j] = dp_sum[i-1][j] + dp_sum[i][j-1] - dp_sum[i-1][j-1]
            dp_sum[i][j] %= mod
#print(dp_sum)
print(dp_sum[n-1][m-1]+1)#空集合で+1

