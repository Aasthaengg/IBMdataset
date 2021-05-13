import sys

def solve():
    input = sys.stdin.readline
    mod = 7 + 10 ** 9
    N, M = map(int, input().split())
    S = [int(s) for s in input().split()]
    T = [int(t) for t in input().split()]

    DP = [[0 for j in range(M+1)] for i in range(N + 1)]
    DP[0] = [1] * (M + 1)
    for i in range(1, N + 1): DP[i][0] = 1
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                DP[i+1][j+1] = (DP[i+1][j] + DP[i][j+1]) % mod
            else: 
                DP[i+1][j+1] = (DP[i+1][j] + DP[i][j+1] - DP[i][j]) % mod
    print(DP[N][M])
    return

if __name__ == "__main__":
    solve()