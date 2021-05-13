n, m, q = map(int,input().split())
bord = [[0 for _j in range(n+2)] for _i in range(n+2)]

for _i in range(m):
    left, right = map(int, input().split())
    bord[left][right] += 1

for i in range(1, n+2):
    for j in range(1, n+2):
        bord[i][j] += bord[i][j-1]

result = []
for _i in range(q):
    p, q = map(int, input().split())
    c = 0
    for i in range(p, q+1):
        c += bord[i][q]-bord[i][p-1]
    result.append(c)
print(*result)