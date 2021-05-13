def warshall_floyd():
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])

H, W = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(10)]
warshall_floyd()
res = 0
for _ in range(H):
    A = list(map(int, input().split()))
    res += sum(C[a][1] for a in A if a != -1)
print(res)