


N,M = map(int, input().split())
xyz = [tuple(map(int, input().split())) for _ in range(N)]

cakes = [[] for _ in range(1 << 3)]

for bit in range(1 << 3):
    for i in range(N):
        total = 0
        for j in range(3):
            if bit & (1 << j):
                total += -1 * xyz[i][j]
            else:
                total += xyz[i][j]

        cakes[bit].append((total, xyz[i][0], xyz[i][1], xyz[i][2]))


ans = []
for i in range(1 << 3):
    total = 0
    cakes[i].sort(reverse=True)
    x,y,z = 0,0,0
    #print("-----",cakes[i])
    for j in range(M):
        x += cakes[i][j][1]
        y += cakes[i][j][2]
        z += cakes[i][j][3]


    ans.append(abs(x) + abs(y) + abs(z))

print(max(ans))

#print(ans)
