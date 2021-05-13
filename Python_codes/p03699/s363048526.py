import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    DP = [[False for j in range(100 * N + 1)] for _ in range(N)]
    DP[0][0] = True
    S = [int(input()) for _ in range(N)]
    DP[0][S[0]] = True
    for i in range(1, N):
        for j in range(100 * N + 1):
            if DP[i-1][j] == True: 
                DP[i][j] = True
                if j + S[i] < 100 * N + 1: DP[i][j + S[i]] = True
    for i in reversed(range(100 * N + 1)):
        if DP[N-1][i] and i % 10 > 0:
            print(i)
            break
    else: print(0)

    return 0

if __name__ == "__main__":
    solve()