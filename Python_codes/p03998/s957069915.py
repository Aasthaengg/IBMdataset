a = input()
b = input()
c = input()
li=["a","b","c"]
turn = 0
for i in range(300):
    if turn == 0:
        if a == "":
            print("A")
            exit()
        else:
            turn = li.index(a[0])
            a = a[1:]
    elif turn == 1:
        if b == "":
            print("B")
            exit()
        else:
            turn = li.index(b[0])
            b = b[1:]
    else:
        if c == "":
            print("C")
            exit()
        else:
            turn = li.index(c[0])
            c = c[1:]
