N,M = list(map(int,input().split(" ")))
As = list(map(int,input().split(" ")))

# N → 10^4 数字0-9 → 10^5

match= [-1,2,5,5,4,5,6,3,7,6]

dp = [-1 for _ in range(N + 100)] #N 本使ったときの最大値
dp[0] = 0
for num in As:
    dp[match[num] ]  = 1

for i in range(N + 1):
    for num in As:
        match_num = match[num]
        if i - match_num >= 0:
            #数字numを使うときのマッチの本数
            dp[i] = max( dp[i - match_num] + 1 , dp[i])
# print(dp)

ans = []
cot = N
As.sort(reverse=True)
while True:
    if cot == 0:
        break
    for num in As:
        if dp[cot - match[num]]  == dp[cot] - 1:
            ans.append(str(num))
            cot -= match[num]
            break
print("".join(ans))