N = int(input())
dp = [0 for i in range(N + 1)]
divider = [1]

i = 6
while i <= N:
    divider.append(i)
    i *= 6

i = 9
while i <= N:
    divider.append(i)
    i *= 9


for x in divider:
    dp[x] = 1

for i in range(1, N + 1):
    if dp[i] == 0:
        poss = []
        for x in divider:
            if i - x >= 0:
                poss.append(dp[i - x] + 1)
        dp[i] = min(poss)

print(dp[N])
