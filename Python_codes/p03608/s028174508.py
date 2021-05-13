from itertools import permutations
n, m, r = map(int, input().split())
towns = [int(x) - 1 for x in input().split()]
inf = 10 ** 10
d = [[inf for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c

def warshall_floyd(d, v):
    for k in range(v):
        for i in range(v):
            for j in range(v):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

warshall_floyd(d, n)
ans = 10 ** 10
for t in permutations(towns):
    tmp = 0
    for i in range(len(t) - 1):
        tmp += d[t[i]][t[i+1]]
    ans = min(ans, tmp)


print(ans)