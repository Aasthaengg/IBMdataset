


def main():
    data = list(input())
    # dp = [[0 for i in range(4)] for i in range(len(data) + 1)]
    # dp[len(data)][3] += 1

    dp = [0, 0, 0, 1]
    mod = 10 ** 9 + 7

    dic = {0:'A', 1:'B', 2:'C'}
    for i in range(len(data))[::-1]:
        element = data[i]
        for j in range(4):
            if j == 3:
                if element == '?':
                    dp[j] *= 3
            else:
                if dic[j] == element:
                    dp[j] += dp[j + 1]

                elif element == '?':
                    dp[j] = dp[j] * 3 + dp[j + 1]

            dp[j] %= mod



    print(dp[0] % mod)





if __name__ == '__main__':
    main()
