h, w = map(int,input().split())
s_l = []
for i in range(h):
    s_l.append(list(input()))
    for j in range(w):
        if s_l[i][j] == '.':
            s_l[i][j] = 0
        else:
            s_l[i][j] = 1

dp = []
for _ in range(h):
    dp.append([0] * w)

if s_l[0][0] != 0:
    dp[0][0] += 1

for i in range(1,h):
    if dp[i-1][0]%2 != s_l[i][0]:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
for j in range(1,w):
    if dp[0][j-1]%2 != s_l[0][j]:
        dp[0][j] = dp[0][j-1] + 1
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1,h):
    for j in range(1,w):
        if dp[i-1][j]%2 != s_l[i][j]:
            plus_i = 1
        else:
            plus_i = 0
        if dp[i][j-1]%2 != s_l[i][j]:
            plus_j = 1
        else:
            plus_j = 0
        dp[i][j] = min(dp[i-1][j] + plus_i, dp[i][j-1] + plus_j)

#print(dp)
print((dp[h-1][w-1]+1)//2)