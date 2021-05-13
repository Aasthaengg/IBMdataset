H, W= map(int, input().split())
minpath = [[float("inf")]*10 for _ in range(10)]
path = [list(map(int, input().split())) for i in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            path[j][k] = min(path[j][k], path[j][i]+path[i][k])
ans = 0
for i in range(H):
    A = list(map(int, input().split()))
    for j in range(W):
        if A[j] == -1 or A[j] == 1:
            continue
        else:
            ans += path[A[j]][1]
print(ans)
            


