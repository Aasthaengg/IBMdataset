a = list(input())
b = list(input())
c = list(input())
dum = a.pop(0)
for i in range(300):
    if dum == "a":
        if len(a) != 0:
            dum = a.pop(0)
        else:
            print("A")
            exit()
    elif dum == "b":
        if len(b) != 0:
            dum = b.pop(0)
        else:
            print("B")
            exit()
    else:
        if len(c) != 0:
            dum = c.pop(0)
        else:
            print("C")
            exit()
