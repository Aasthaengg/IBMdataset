h, w = [int(i) for i in input().split()]
s = [input() for j in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            continue
        f = False
        if j > 0:
            if s[i][j-1] == "#":
                f = True
        if j < w-1:
            if s[i][j+1] == "#":
                f = True
        if i > 0:
            if s[i-1][j] == "#":
                f = True
        if i < h-1:
            if s[i+1][j] == "#":
                f = True
        if not f:
            print("No")
            exit()
print("Yes")