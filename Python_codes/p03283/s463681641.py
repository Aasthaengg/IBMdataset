n, m, q = map(int, input().split())
lr = []
for i in range(m):
    l, r = map(int, input().split())
    lr.append((l, r))

mtx = [[0 for i in range(n)] for j in range(n)]

for item in lr:
    mtx[item[0]-1][item[1]-1] += 1

rui = [[0 for i in range(n+1)] for j in range(n+1)]

for i in range(n):
    for j in range(n):
        rui[i+1][j+1] = rui[i][j+1] + rui[i+1][j] - rui[i][j] + mtx[i][j]

for i in range(q):
    p, q = map(int, input().split())
    p -= 1
    output = rui[q][q] - rui[p][q] - rui[q][p] + rui[p][p]
    print(output)
