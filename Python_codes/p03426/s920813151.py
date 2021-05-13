H, W, D = map(int, input().split(" "))
coord = {}

for i in range(H):
    for j, A in enumerate(map(int, input().split(" "))):
        coord[A] = (i, j)

magic = [0 for i in range(H * W + 1)]
for i in range(H * W + 1):
    if i + D <= H * W:
        magic[i + D] += magic[i]
        if i != 0:
            magic[i + D] += abs(coord[i][0] - coord[i + D][0]) + abs(coord[i][1] - coord[i + D][1])

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split(" "))
    print(magic[R] - magic[L])