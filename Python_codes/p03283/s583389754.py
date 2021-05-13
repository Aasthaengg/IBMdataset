
def resolve():
    N, M, Q = list(map(int, input().split()))
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    acc = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for lr in LR:
        l, r = lr
        acc[l][r] += 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            acc[i][j] += acc[i][j-1]
    for i in range(1, N+1):
        for j in range(1, N+1):
            acc[i][j] += acc[i-1][j]
    
    for pq in PQ:
        p, q = pq
        print(acc[q][q] - acc[p-1][q] - acc[q][p-1] + acc[p-1][p-1])


if '__main__' == __name__:
    resolve()