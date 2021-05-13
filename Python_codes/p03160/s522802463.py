def input_li():
    return list(map(int, input().split()))

def input_int():
    return int(input())

N = input_int()
h_li = input_li()
dp = [0] * N
dp[0] = 0
dp[1] = abs(h_li[1] - h_li[0])
for i in range(2, N):
    dp[i] = min(
        dp[i - 1] + abs(h_li[i] - h_li[i - 1]),
        dp[i - 2] + abs(h_li[i] - h_li[i - 2])
    )
print(dp[-1])
