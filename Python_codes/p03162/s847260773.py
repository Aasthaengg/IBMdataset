n = int(input())
dp = [0, 0, 0]
for x in range(n):
    new_dp = [0]*3
    happy = [int(x) for x in input().split()]
    for y in range(3):
        for z in range(3):
            if y != z:
                new_dp[y] = max(new_dp[y], dp[z] + happy[y])
    dp = new_dp
print(max(dp[0], dp[1], dp[2]))