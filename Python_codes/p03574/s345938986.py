h, w = [int(w) for w in input().split()]
ls = [input() for _ in range(h)]


def search(th, tw):
    t = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if not 0 <= th+i < h:
                continue
            if not 0 <= tw+j < w:
                continue
            if ls[th+i][tw+j] == "#":
                t += 1
    return t


ans = ""
for i in range(h):
    for j in range(w):
        if ls[i][j] == "#":
            ans += "#"
        else:
            ans += str(search(i, j))
    ans += "\n"

print(ans)
