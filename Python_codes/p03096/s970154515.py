def main():
    MOD = 10**9 + 7
    N = int(input())
    C = [int(input()) - 1 for _ in range(N)]
    if N == 1:
        print(1)
        return
    # |---|
    # 1-2-1-2-2
    #   |---|
    latest_indices = [-1] * (2 * (10**5))
    next_indices = [-1] * N
    for cur_index, c in enumerate(C):
        latest_index = latest_indices[c]
        if latest_index >= 0:
            next_indices[latest_index] = cur_index
        latest_indices[c] = cur_index
    dp = [0] * N
    dp[0] = 1
    for cur_index in range(N - 1):
        next_index = next_indices[cur_index]
        if next_index > cur_index + 1:
            dp[next_index] += dp[cur_index]
            dp[next_index] %= MOD
        dp[cur_index + 1] += dp[cur_index]
        dp[cur_index + 1] %= MOD
    print(dp[N - 1])


if __name__ == '__main__':
    main()