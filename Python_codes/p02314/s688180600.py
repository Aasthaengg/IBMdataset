def get_number_of_coin(coins, dp_coin, total):
    for c in coins:
        for j in range(c, total + 1):
            dp_coin[j] = min(dp_coin[j], dp_coin[j - c] + 1)
    return dp_coin[-1]


if __name__ == "__main__":
    total, n_coin = map(int, input().split())
    *coins, = map(int, input().split())    
    dp_coin = [10000] * (total + 1)
    dp_coin[0] = 0
    print(get_number_of_coin(coins, dp_coin, total))
