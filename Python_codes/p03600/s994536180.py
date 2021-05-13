N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

flag = [[0] * N for _ in range(N)]
dist = [line[:] for line in A]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or j == k or k == i:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
            elif dist[i][j] < dist[i][k] + dist[k][j]:
                flag[i][j] += 1

if A != dist:
    print(-1)
    exit()

ans = 0
for i in range(N):
    for j in range(N):
        if flag[i][j] == N-2:
            ans += A[i][j]

ans //= 2
print(ans)