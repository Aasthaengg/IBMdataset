import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    if A[0] != 0:
        print(-1)
        return
    dp = [0] * N
    for i in range(1, N):
        if A[i] > A[i-1] + 1:
            print(-1)
            return
        elif A[i] == A[i-1] + 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1] + A[i]
    
    print(dp[-1])

if __name__ == "__main__":
    main()