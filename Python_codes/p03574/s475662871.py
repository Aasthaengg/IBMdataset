import copy
H, W = list(map(int, input().split()))
tb = []
for h in range(H+2):
    line = []
    if h == 0 or h == H+2-1:
        for w in range(W+2):
            line.append(0)
    else:
        line = list("." + input() + ".")
        for w in range(W+2):
            if line[w] == ".":
                line[w] = 0
    tb.append(line)
#def xxx(): [print("".join(list(map(str,line)))) for line in tb];print()
#xxx()


for i in range(1,H+1):
    for j in range(1,W+1):
        if tb[i][j] != "#":
            if tb[i-1][j] == "#": tb[i][j] += 1
            if tb[i+1][j] == "#": tb[i][j] += 1
            if tb[i][j-1] == "#": tb[i][j] += 1
            if tb[i][j+1] == "#": tb[i][j] += 1
            if tb[i-1][j-1] == "#": tb[i][j] += 1
            if tb[i-1][j+1] == "#": tb[i][j] += 1
            if tb[i+1][j-1] == "#": tb[i][j] += 1
            if tb[i+1][j+1] == "#": tb[i][j] += 1

#xxx()
[print("".join(list(map(str,line)))[1:-1]) for i,line in enumerate(tb) if 0 < i < H+2-1];print()