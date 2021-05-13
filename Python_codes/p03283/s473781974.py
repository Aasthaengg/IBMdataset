def main():
    N, M, Q = list(map(int, input().split(' ')))
    x = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        left, right = list(map(int, input().split(' ')))
        x[left - 1][right - 1] += 1
    for i in range(N):
        for j in range(1, N):
            x[i][j] += x[i][j - 1]
    for j in range(N):
        for i in range(N - 2, -1, -1):
            x[i][j] += x[i + 1][j]
    queries = [list(map(int, input().split(' '))) for _ in range(Q)]
    for q in queries:
        print(x[q[0] - 1][q[1] - 1])


if __name__ == '__main__':
    main()