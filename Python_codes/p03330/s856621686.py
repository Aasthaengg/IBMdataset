
n,c = map(int, input().split())
d = []
for _ in range(c):
    a = list(map(int, input().split()))
    d.append(a)

grid = [[0 for j in range(c+1)] for i in range(3)]
for i in range(n):
    for j,cc in enumerate(map(int, input().split())):
        k = j
        grid[(i+j)%3][cc] += 1

ans = float('INF')

for i in range(1,c+1):
    for j in range(1,c+1):
        if i == j:
            continue
        for k in range(1,c+1):
            if i == k or j == k:
                continue
            cost = 0
            for a in range(1,c+1):
                # print(int(d[a-1][i-1]), grid[0][a], int(d[a-1][j-1]), grid[1][a], int(d[a-1][k-1]), grid[2][a])
                cost += d[a-1][i-1] * grid[0][a] + d[a-1][j-1] * grid[1][a] + d[a-1][k-1] * grid[2][a]
            
            if cost < ans:
                # print(i,j,k,cost)
                ans = cost

print(int(ans))
