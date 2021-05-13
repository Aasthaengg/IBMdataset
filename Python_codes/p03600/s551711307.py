def warshall_floyd(G):
    import copy
    ret = copy.deepcopy(G)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ret[i][j] = min(ret[i][j], ret[i][k] + ret[k][j])
    return ret


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
W, ans = warshall_floyd(A), 0
if A == W:
    for i in range(N):
        for j in range(N):
            if sum([A[i][j] == A[i][k] + A[k][j] for k in range(N) if k != i and k != j]) == 0:
                ans += A[i][j]
    print(ans // 2)
else:
    print(-1)
