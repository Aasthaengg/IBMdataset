import sys

def input():
    return sys.stdin.readline().strip()

def main():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))

    dp = [0] * N
    dp[1] = abs(H[1] - H[0])
    for i in range(2,N):
        dp[i] = min(dp[j] + abs(H[i] - H[j]) for j in range(max(0,i-K),i))
    print(dp[-1])

if __name__ == "__main__":
    main()