from bisect import bisect_right
n = int(input())
MX = 100010
dp = [float('inf') for _ in range(MX)]
dp[0] = 0
pow_6, pow_9 = [6], [9]
while True:
    flg = False
    if pow_6[-1]*6 <= MX:
        pow_6.append(pow_6[-1]*6)
        flg = True
    if pow_9[-1]*9 <= MX:
        pow_9.append(pow_9[-1]*9)
        flg = True
    
    if flg == False:
        break

for i in range(1, MX):
    tmp = [1]
    if i >= 6:
        x = bisect_right(pow_6, i)
        tmp.append(pow_6[x-1])
    if i >= 9:
        y = bisect_right(pow_9, i)
        tmp.append(pow_9[y-1])
    for t in tmp:
        dp[i] = min(dp[i], dp[i-t]+1)
print(dp[n])