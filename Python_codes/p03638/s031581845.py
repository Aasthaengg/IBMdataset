H, W = map(int, input().split())
N = int(input())
c = [[0]*W for _ in range(H)]
a = list(map(int, input().split()))
colors = []
for i in range(N-1, -1, -1):
    colors += [i+1]*a[i]

route = []
for h in range(H):
    tmp = []
    for w in range(W):
        tmp.append((h, w))
    if h % 2 == 0:
        route += tmp
    else:
        route += tmp[::-1]

for i in range(H*W):
    x, y = route[i]
    c[x][y] = colors.pop()

for row in c:
    print(*row)