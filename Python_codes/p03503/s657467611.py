def main():
    n = int(input())
    F = [list(map(int, input().split())) for _ in range(n)]
    P = [list(map(int, input().split())) for _ in range(n)]
    ans = -float('inf')
    for i in range(1, 1 << 10):
        A = [0] * 10
        for j in range(10):
            if i >> j & 1:
                A[j] = 1
        C = [0] * n
        for k in range(n):
            c = 0
            for a, f in zip(A, F[k]):
                if a == f == 1:
                    c += 1
            C[k] = c
        ans = max(ans, sum([P[i][c] for i, c in enumerate(C)]))
    print(ans)


if __name__ == '__main__':
    main()
