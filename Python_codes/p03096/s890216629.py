from collections import defaultdict

def main():
    num = int(input())
    data = [int(input()) for i in range(num)]

    dic = defaultdict(int)
    mod = 10 ** 9 + 7
    dp = [1 for i in range(num + 1)]

    for i in range(num):
        if i != 0:
            if data[i] == data[i - 1]:
                dp[i + 1] = dp[i]
                continue

        now_num = data[i]
        dp[i + 1] = (dp[i] + dic[now_num]) % mod
        dic[now_num] += dp[i]
        dic[now_num] %= mod

    print(dp[num])

if __name__ == '__main__':
    main()
