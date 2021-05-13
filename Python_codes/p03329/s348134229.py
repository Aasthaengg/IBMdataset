N = int(input())

# dp[i] i円引き出すのに必要な手数
dp = [101010] * 201010
money = [1]
t = 6
q = 9
while t <= N:
    money.append(t)
    t*=6
while q <= N:
    money.append(q)
    q*=9

for m in money:
    dp[m] = 1

for i in range(1,N):
    for m in money:
        dp[i+m] = min(dp[i+m], dp[i]+1)

print(dp[N])