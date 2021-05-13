def main():
    n, m, l = map(int, input().split())
    A, B = [], []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    for _ in range(m):
        B.append(list(map(int, input().split())))
    C = [[0] * l for _ in range(n)]
    for i in range(n):
        for j in range(l):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(m))
    for line in C:
        print(' '.join(map(str, line)))


if __name__ == '__main__':
    main()

