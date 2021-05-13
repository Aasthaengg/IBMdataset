n, m, q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]
query = [list(map(int, input().split())) for _ in range(q)]

trains = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    l, r = lr[i]
    trains[l][r] += 1

for i in range(n+1):
    for j in range(n):
        trains[i][j+1] += trains[i][j]

for j in range(n+1):
    for i in range(n):
        trains[i+1][j] += trains[i][j]

for i in range(q):
    p, q = query[i]
    print(trains[q][q]-trains[p-1][q]-trains[q][p-1]+trains[p-1][p-1])