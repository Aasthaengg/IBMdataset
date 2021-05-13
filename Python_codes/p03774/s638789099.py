N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
C = [list(map(int, input().split())) for _ in range(M)]

for n in range(N):
    d_lst = []
    for m in range(M):
        dis = abs(A[n][0] - C[m][0]) + abs(A[n][1] - C[m][1])
        d_lst.append(dis)
    print(d_lst.index(min(d_lst)) + 1)