a = input()
b = input()
c = input()

cur = "a"

while True:
    if cur == "a":
        if len(a) == 0:
            print("A")
            break
        else:
            cur = a[0]
            a = a[1:]
    elif cur == "b":
        if len(b) == 0:
            print("B")
            break
        else:
            cur = b[0]
            b = b[1:]
    else:
        if len(c) == 0:
            print("C")
            break
        else:
            cur = c[0]
            c = c[1:]