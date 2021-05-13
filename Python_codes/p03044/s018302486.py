N, *m=map(int, open(0).read().split())

im = iter(m)
UVW = list(zip(im, im, im))

# set default color to -1

colors = {i:-1 for i in range(1,N+1)}
u,v,w = UVW[0]
colors[u] = 0

def opposite(u, v):
    if v == -1:
        return u
    if v == 0:
        return 1
    if v == 1:
        return 0

def same(u, v):
    if v == -1:
        return u
    else:
        return v

while -1 in colors.values():
    next_UVW = []
    for u, v, w in UVW:
        if colors[u] == -1 and colors[v] == -1:
            next_UVW.append((u, v, w))
            continue

        if w % 2 == 0:
            colors[u] = same(colors[u], colors[v])
            colors[v] = same(colors[v], colors[u])

        if w % 2 == 1:
            colors[u] = opposite(colors[u], colors[v])
            colors[v] = opposite(colors[v], colors[u])

        if colors[u] == -1 or colors[v] == -1:
            next_UVW.append((u,v,w))

    UVW = next_UVW



for i in range(1, N+1):
    print(colors[i])