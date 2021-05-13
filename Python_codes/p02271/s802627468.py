n = int(input())
a = [int(_) for _ in input().split()]
m = int(input())
b = [int(_) for _ in input().split()]

dp = [[False for i in range(4300)]for i in range(2)]
dp[0][0] = True
dp[1][0] = True
c = False
for i in a:
    for j in range(4000):
        if dp[c][j]:
            dp[not(c)][j+i] = True
            dp[not(c)][j] = True
    c = not(c)

for i in b:
    if dp[c][i]:
        print("yes")
    else:
        print("no")

# print(dp[c][:20])

