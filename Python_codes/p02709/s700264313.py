import sys

def solve():
    input = sys.stdin.readline
    N = int(input())
    A = [int(a) for a in input().split()]
    B = [(A[i], i) for i in range(N)]
    B.sort(reverse = True)

    DP = [[-1 for j in range(N + 1)] for _ in range(N)] #i番目の幼児まで見た時、左からi番目まで埋まっている時の最大値
    DP[0][0] = B[0][0] * abs(B[0][1] - (N - 1))
    DP[0][1] = B[0][0] * B[0][1]

    for i in range(1, N):
        for j in range(i + 1):
            #右に詰める時はjの値は変わらない
            #左に詰めるときはj += 1
            DP[i][j] = max(DP[i][j], DP[i-1][j] + B[i][0] * abs(B[i][1] - (N - 1 - i + j)))
            DP[i][j+1] = max(DP[i][j+1], DP[i-1][j] + B[i][0] * abs(B[i][1] - j))
    print(max(DP[N-1]))

    return 0

if __name__ == "__main__":
    solve()