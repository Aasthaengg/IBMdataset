def input_li():
    return list(map(int, input().split()))

def input_int():
    return int(input())

N, K = input_li()
h_li = input_li()
dp = [10 ** 9 + 7] * N
dp[0] = 0
for i in range(N):
    for j in range(1, K + 1):
        if i + j < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h_li[i] - h_li[i + j]))
print(dp[-1])
