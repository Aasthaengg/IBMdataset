import sys

sys.setrecursionlimit(10 ** 9)


# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    P = list(map(float,input().split()))

    dp = [[0 for _ in range(N+1)] for i in range(N+1)]   #i枚投げたときの　j表が出た枚　のdpが確立
    dp[0][0] =1
    for i in range(1,N+1):
        for j in range(0,i+1):
            dp[i][j] = dp[i-1][j] * (1-P[i-1]) + dp[i-1][j-1]*P[i-1]

    n = (N+1)//2

    print(sum(dp[N][n:]))
    pass

if __name__ == "__main__":
    main()
