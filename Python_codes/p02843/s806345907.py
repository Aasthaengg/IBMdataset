X = int(input())
dp = [False for _ in range(X+1)]
dp[0] = True
for x in range(X+1):
    if x > 99:
        item = [100, 101, 102, 103, 104, 105]
        for i in item:
            if dp[x-i]:
                dp[x] = True
if dp[X]:
    print(1)
else:
    print(0)