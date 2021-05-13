import sys

s = sys.stdin.readline().strip()
x, y = map(int, sys.stdin.readline().split())

goal = {"x": x, "y": y}
dist = {"x": [], "y": []}

if s[-1] != "T":
    s += "T"
d = 0
f = 0
x_init = -1
for i in s:
    if i == "F":
        d += 1
    else:
        if f % 2 == 0:
            if x_init == -1:
                x_init = d
            else:
                dist["x"].append(d)
        else:
            dist["y"].append(d)
        d = 0
        f += 1

# print(dist)
for mode in ("x", "y"):
    len_d = len(dist[mode])
    cand = set()
    if mode == "x":
        cand.add(x_init)
    else:
        cand.add(0)
    for i in range(len_d):
        next_cand = set()
        for d in cand:
            next_cand.add(d + dist[mode][i])
            next_cand.add(d - dist[mode][i])
        cand = next_cand

    if goal[mode] not in cand:
        print("No")
        sys.exit()

print("Yes")