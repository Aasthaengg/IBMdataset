n = int(input())
edges = [list(map(int, input().split())) for _ in range(n)]
need_of_routes = [[True]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        if i == k:
            continue
        for j in range(n):
            if j == i or j == k:
                continue

            if edges[i][j] > edges[i][k] + edges[k][j]:
                print(-1)
                exit()
            elif edges[i][j] == edges[i][k] + edges[k][j]:
                need_of_routes[i][j] = False

count = 0
for i in range(n):
    for j in range(n):
        if need_of_routes[i][j]:
            count += edges[i][j]

print(count//2)