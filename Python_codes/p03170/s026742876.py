def main():
    N, K = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    dp = [0 for _ in range(K + 1)]  # whether Taro wins
    for n in range(1, K + 1):
        win = 0
        for a in A:
            if n - a >= 0 and dp[n - a] == 0:
                win = 1
                break
        dp[n] = win
    print('First' if dp[K] == 1 else 'Second')


if __name__ == '__main__':
    main()