import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7

def main():
    N = int(readline())
    coin = [6**i for i in range(10) if 6**i <= N]
    coin += [9**i for i in range(10) if 9**i <= N]
    coin.sort()
    dp = [INF]*(N+1)
    dp[0]=0
    for c in coin:
        for i in range(N+1):
            if i>=c:
                dp[i] = min(dp[i-c]+1, dp[i])
    print(dp[-1])


if __name__ == '__main__':
    main()