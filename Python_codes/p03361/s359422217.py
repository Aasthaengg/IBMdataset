h, w = [int(w) for w in input().split()]
lls = [input() for w in range(h)]

lls = ["."*(w+2)]+["."+w+"."for w in lls] + ["."*(w+2)]
# N E S W
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cond = True
for i in range(1, h+2):
    for j in range(1, w+2):
        if lls[i][j] == ".":
            continue
        nb = False
        for d1, d2 in direction:
            if lls[i+d1][j+d2] == "#":
                nb = True
        if nb == False:
            cond = False

        now_dir = 0

print("Yes" if cond else "No")
