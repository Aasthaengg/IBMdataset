N, M = map(int, input().split())
a = [list(map(int, input().split())) for i in range(M)]
r = [0]*N
for i in range(M):
    r[a[i][0] - 1] += 1
    r[a[i][1] - 1] += 1
for i in range(N):
    print(r[i])
