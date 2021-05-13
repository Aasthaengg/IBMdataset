g = []

for i in range(3):
    g.append(list(map(int, input().split())))

for i in range(1,3):
    offset = g[i][0] - g[0][0]
    if not ((g[i][1] - g[0][1] == offset) and (g[i][2] - g[0][2] == offset)):
        print("No")
        exit()

print("Yes")