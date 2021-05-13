h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
l = [["#"] for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            l[i].append(0)
        else:
            l[i].append("#")
    l[i].append("#")
l = [["#" for i in range((w+2))]] + l + [["#" for i in range(w+2)]]
pos = []
for i in range(1, h+1):
    for j in range(1, w+1):
        if l[i][j] == "#":
            pos.append([i, j])
for i in pos:
    x, y = i
    for j in [[x-1, y-1], [x, y-1], [x+1, y-1], [x-1, y], [x+1, y], [x-1, y+1], [x, y+1], [x+1, y+1]]:
        if l[j[0]][j[1]] != "#":
            l[j[0]][j[1]] += 1
for i in range(1, h+1):
    print("".join(list(map(str, l[i][1:-1]))))