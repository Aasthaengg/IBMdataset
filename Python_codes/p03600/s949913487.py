N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]
roads = [[True]*N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if A[i][j] > A[i][k]+A[j][k]:
                print(-1)
                exit()
            if i == j:
                roads[i][j] = False
            if i != k and j != k and A[i][j] == A[i][k]+A[j][k]:
                roads[i][j] = False


ans = 0
for i in range(N):
    for j in range(i+1, N):
        if roads[i][j] is True:
            ans += A[i][j]
print(ans)
