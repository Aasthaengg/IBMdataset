INF = 10 ** 7
def main():
    N,M = map(int,input().split())
    coin = list(map(int,input().split()))
    dp = [INF] * (N + 1)
    dp[0] = 0
    for c in coin:
        for i in range(c,N + 1):
            dp[i] = min(dp[i],dp[i - c] + 1)
    print(dp[-1])
if __name__ == '__main__':
    main()

