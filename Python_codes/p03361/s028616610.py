H, W = map(int, input().split())
s = [input() for _ in range(H)]

def f():
    a = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for h in range(H):
        for w in range(W):

            if s[h][w] == "#":
                f = True
                for x, y in a:
                    h2 = h + x
                    w2 = w + y
                    if 0 <= h2 < H and 0 <= w2 < W:
                        if s[h2][w2] == "#":
                            f = False
                if f:
                    print("No")
                    return
    print("Yes")
    return

f()