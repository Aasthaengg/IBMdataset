sa = list(input())
sb = list(input())
sc = list(input())
mode = "a"
while True:
    if mode == "a":
        if len(sa) == 0:
            print("A")
            exit()
        mode = sa.pop(0)
    elif mode == "b":
        if len(sb) == 0:
            print("B")
            exit()
        mode = sb.pop(0)
    elif mode == "c":
        if len(sc) == 0:
            print("C")
            exit()
        mode = sc.pop(0)
