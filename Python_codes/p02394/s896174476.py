inps = input().split()
if len(inps) < 5:
    print("Illegal input.")
else:
    w = int(inps[0])
    h = int(inps[1])
    x = int(inps[2])
    y = int(inps[3])
    r = int(inps[4])
    if x - r < 0 or x + r > w:
        print("No")
    elif y - r < 0 or y + r > h:
        print("No")
    else:
        print("Yes")