import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]

    dp = [0] * (N+1)
    
    for i in range(N):
        dp[A[i]] = dp[A[i]-1] + 1

    print(N - max(dp))


if __name__ == "__main__":
    main()