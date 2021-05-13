def next_pos(x, y, W):
    if x % 2 == 0 and y == W - 1:
        return (x + 1, y)
    elif x % 2 == 0:
        return (x, y + 1)
    elif y == 0:
        return (x + 1, y)
    else:
        return (x, y - 1)


def solve(a, H, W):
    x, y = 0, 0
    c = [[""] * W for _ in range(H)]
    for i, v in enumerate(a):
        for _ in range(v):
            c[x][y] = str(i + 1)
            x, y = next_pos(x, y, W)
    return c


H, W = map(int, input().split())
N = int(input())
a = map(int, input().split())

for row in solve(a, H, W):
    print(" ".join(row))
