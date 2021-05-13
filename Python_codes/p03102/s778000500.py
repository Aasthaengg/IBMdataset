N, M, C = map(int, input().split())
vecB = list(map(int, input().split()))
matA = [list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N):
    value = 0
    for j in range(M):
        value += matA[i][j] * vecB[j]
    value += C
    if value > 0:
       	ans += 1
print(ans)