
def warshall_floyd(cost):
    ret = [[1]*N for _ in [0]*N]
    for k in range(N):
        for i, c_left in enumerate(cost[i][k] for i in range(N)):
            for j, (c_now, c_right) in enumerate(zip(cost[i], cost[k])):
                if c_left + c_right < c_now:
                    print(-1)
                    exit()
                if i == j or j == k or k == i:
                    continue
                if c_left + c_right == c_now:
                    ret[i][j] = ret[j][i] = 0
    return ret


INF = 10**10
N, *A = map(int, open(0).read().split())
*A, = zip(*[iter(A)]*N)


E = []
for i in range(N):
    for j in range(i+1, N):
        E.append((A[i][j], i, j))
E.sort()

road = warshall_floyd(A)
ans = 0
for cost, i, j in E:
    if not road[i][j]:
        continue
    ans += cost

print(ans)
