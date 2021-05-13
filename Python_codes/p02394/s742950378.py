import fileinput

for line in fileinput.input():
    tokens = list(map(int, line.strip().split()))
    W, H, x, y, r = tokens[0], tokens[1], tokens[2], tokens[3], tokens[4]

    flag = True
    if x - r < 0:
        flag = False
    if x + r > W:
        flag = False
    if y - r < 0:
        flag = False
    if y + r > H:
        flag = False

    if flag:
        print("Yes")
    else:
        print("No")