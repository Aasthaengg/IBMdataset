INF = int(1e9) + 7
h, w = map(int, input().split())
s = []
for i in range(h):
    s.append(list(input()))

dp = [[INF] * w for i in range(h)]
if s[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0
#print(dp)

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            continue
        val1 = dp[i-1][j]
        if s[i][j] == '#' and s[i-1][j] == '.':
            val1 += 1
        val2 = dp[i][j-1]
        if s[i][j] == '#' and s[i][j-1] == '.':
            val2 += 1
        dp[i][j] = min(val1, val2)
        #print(i, j,val1, val2)
print(dp[h-1][w-1])
#print(dp)
