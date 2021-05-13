r, c = map(int, input().split())
ans = 0

map = []
for i in range(r):
    map.append(input())

L = [[0]*c for i in range(r)]
R = [[0]*c for i in range(r)]
D = [[0]*c for i in range(r)]
U = [[0]*c for i in range(r)]

for i in range(r):
    for j in range(c):
        if map[i][j] == ".":
            L[i][j] = L[i][j - 1] + 1
        else:
            L[i][j] = 0
for i in range(r):
    for j in range(c - 1, -1, -1):
        if j == c - 1:
            if map[i][j] == ".":
                R[i][j] = 1
            continue
        if map[i][j] == ".":
            R[i][j] = R[i][j + 1] + 1
        else:
            R[i][j] = 0
for i in range(r):
    for j in range(c):
        if map[i][j] == ".":
            D[i][j] = D[i - 1][j] + 1
        else:
            D[i][j] = 0
for i in range(r - 1, -1, -1):
    for j in range(c):
        if i == r - 1:
            if map[i][j] == ".":
                U[i][j] = 1
            continue
        if map[i][j] == ".":
            U[i][j] = U[i + 1][j] + 1
        else:
            U[i][j] = 0

for i in range(r):
    for j in range(c):
        ans = max(ans, L[i][j] + R[i][j] + U[i][j] + D[i][j] - 3)

print(ans)