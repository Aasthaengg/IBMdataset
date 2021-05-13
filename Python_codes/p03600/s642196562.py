def main():
    N = int(input())
    A = [[int(a) for a in input().split()] for _ in range(N)]
    B = [[A[i][j] for j in range(N)] for i in range(N)]
    C = [[A[i][j] for j in range(N)] for i in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                t = B[i][k] + B[k][j]
                if t < B[i][j]:
                    return -1
                if B[i][k] and B[k][j] and t == B[i][j]:
                    C[i][j] = 0
    return sum([sum([C[i][j] for j in range(i)]) for i in range(N)])
print(main())