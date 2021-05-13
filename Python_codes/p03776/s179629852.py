import sys
sys.stdin.readline

def main():
    N, A, B = map(int, input().split())
    V = list(map(int, input().split()))
    DP1 = [[0] * (N + 1) for _ in range((N + 1))]
    DP2 = [[0] * (N + 1) for _ in range((N + 1))]
    DP2[0][0] = 1
    for i in range(1, N+1):
        DP1[i][0] = DP1[i-1][0]
        DP2[i][0] = DP2[i-1][0]
        for j in range(1, N+1):
            if DP2[i-1][j]:
                if DP1[i-1][j] == DP1[i-1][j-1] + V[i-1]:
                    DP1[i][j] = DP1[i-1][j]
                    DP2[i][j] = DP2[i-1][j] + DP2[i-1][j-1]
                elif DP1[i-1][j] > DP1[i-1][j-1] + V[i-1]:
                    DP1[i][j] = DP1[i-1][j]
                    DP2[i][j] = DP2[i-1][j]
                else:
                    DP1[i][j] = DP1[i-1][j-1] + V[i-1]
                    DP2[i][j] = DP2[i-1][j-1]
            elif DP2[i-1][j-1]:
                DP1[i][j] = DP1[i-1][j-1] + V[i-1]
                DP2[i][j] = DP2[i-1][j-1]
    mx = max(DP1[N][n]/n for n in range(A, B+1))
    print(mx)
    print(sum(DP2[N][n] for n in range(A, B+1) if DP1[N][n]/n == mx))

if __name__ == "__main__":
    main()