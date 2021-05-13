def resolve():
    a = input()
    b = input()
    c = input()
    count = "a"
    for i in range(len(a)+len(b)+len(c)):
        if count == "a":
            if len(a) != 0:
                count = a[0]
                a = a[1:]
            else:
                print("A")
                exit()
        elif count == "b":
            if len(b) != 0:
                count = b[0]
                b = b[1:]
            else:
                print("B")
                exit()
        else:
            if len(c) != 0:
                count = c[0]
                c = c[1:]
            else:
                print("C")
                exit()
resolve()