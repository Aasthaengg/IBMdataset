S = input()
N = len(S)

dp = [[0]*2019 for _ in [0]*2]
ans = 0
for i,s in enumerate(S,1):
    s = int(s)
    i %= 2
    dpi = [0]*2019
    dpi1 = dp[1-i]
    dpi[s] += 1
    for j in range(2019):
        dpi[(j*10+s)%2019] += dpi1[j]
    dp[i] = dpi
    ans += dpi[0]

print(ans)
