s = {0}
for i in [*open(0)][1:]:
    a, b = i.split()
    if a == "insert":
        s |= {b}
    else:
        print("yes" if b in s else "no")
