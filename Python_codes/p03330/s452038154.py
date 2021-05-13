N, C = map(int, input().split())
D =[]
for _ in range(C):
    D.append(list(map(int, input().split())))
c = []
for _ in range(N):
    c.append(list(map(int, input().split())))
#print(c)

diago = [[0]*(C + 1) for _ in range(3)]
for i in range(N):
    for j in range(N):
        diago[(i + j) % 3][c[i][j]] += 1
#print(diago)

diff = [[0]*(C+1) for _ in range(3)]

for i, naname in enumerate(diago):
    for color in range(1, C+1):
        for j, cell in enumerate(naname):
            diff[i][color] += D[j-1][color-1] * cell
#print(diff)

candicate = []
for i in range(1, C+1):
    for j in range(1, C+1):
        for k in range(1, C+1):
            if i != j and j != k and k != i:
                candicate.append(diff[0][i]+diff[1][j]+diff[2][k])
print(min(candicate))

