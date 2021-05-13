from math import ceil
def main():
    N = int(input())
    P = list(map(float,input().split()))
    f = [[0]*(N + 1) for _ in range(N + 1)]
    f[0][0] = 1 - P[0]
    f[0][1] = P[0]
    for i in range(1,N):
        p = P[i]
        f[i][0] = f[i - 1][0]*(1 - p)
        for j in range(max(1,ceil((N + 1)/2) - N + i - 3),i + 2):
            f[i][j] += p*f[i - 1][j - 1] + (1 - p)*f[i - 1][j]
    print(sum(f[N - 1][N //2 + 1:]))
    return

if __name__ == "__main__":
    main()