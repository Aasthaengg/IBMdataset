import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]

    dp = [0] * N
    
    for i in range(N):
        if A[i] > 1:
            dp[A[i]-1] = dp[A[i]-2] + 1
        elif A[i] == 1:
            dp[A[i]-1] = 1
    print(N - max(dp))


if __name__ == "__main__":
    main()