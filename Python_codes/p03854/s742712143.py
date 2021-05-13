s = input()
i = 0
while True:
    if s == "":
        print("YES")
        exit(0)
    if i == 0:
        if s[:5] == "dream":
            s = s[5:]
            i = 1
        elif s[:5] == "erase":
            s = s[5:]
            i = 2
        else:
            break
    elif i == 1:
        if s[:5] == "dream":
            s = s[5:]
            i = 1
        elif s[:2] == "er":
            s = s[2:]
            i = 3
        else:
            break
    elif i == 2:
        if s[:5] == "dream":
            s = s[5:]
            i = 1
        elif s[:5] == "erase":
            s = s[5:]
            i = 2
        elif s[:1] == "r":
            s = s[1:]
            i = 0
        else:
            break
    elif i == 3:
        if s[:5] == "dream":
            s = s[5:]
            i = 1
        elif s[:3] == "ase":
            s = s[3:]
            i = 2
        elif s[:5] == "erase":
            s = s[5:]
            i = 2
        else:
            break
print("NO")