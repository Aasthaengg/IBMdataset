H, W = map(int, input().split())
l = []
for h in range(H):
    l.append(input())

j = True
for h in range(H):
    if not j:
        break
    for w in range(W):
        if l[h][w] == "#":
            j = False
            if h != 0:
                if l[h - 1][w] == "#":
                    j = True
            if h != H - 1:
                if l[h + 1][w] == "#":
                    j = True
            if w != 0:
                if l[h][w - 1] == "#":
                    j = True
            if w != W - 1:
                if l[h][w + 1] == "#":
                    j = True
            if not j:
                break
if j:
    print("Yes")
else:
    print("No")
