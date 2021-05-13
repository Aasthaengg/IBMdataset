from copy import deepcopy
N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
B = deepcopy(A)
for u in range(N):
    for v in range(u):
        if u <= v:
            continue
        for w in range(N):
            if w == u or w == v:
                continue
            if A[u][v] > A[u][w]+A[w][v]:
                print(-1)
                exit()
            if A[u][v] == A[u][w]+A[w][v]:
                B[u][v] = 0
                B[v][u] = 0
ans = 0
for i in range(N):
    for j in range(N):
        ans += B[i][j]
print(ans//2)