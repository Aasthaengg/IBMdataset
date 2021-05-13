X = int(input())

Dp = [False for _ in range(X+1)]

Dp[0] = True
for i in range(100, X+1):
    if any([Dp[i - j] == True for j in range(100, 106)]):
        Dp[i] = True
if Dp[X]:
    print(1)
else:
    print(0)