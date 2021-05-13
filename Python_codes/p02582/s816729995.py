a = input()
b = list(a)
if b[0] == "R":
    if b[1] == "R":
        if b[2] == "R":
            print(3)
        else:
            print(2)
    else:
        if b[2] == "R":
            print(1)
        else:
            print(1)
else:
    if b[1] == "R":
        if b[2] == "R":
            print(2)
        else:
            print(1)
    else:
        if b[2] == "R":
            print(1)
        else:
            print(0)
