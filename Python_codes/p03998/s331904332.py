Sa = input()
Sb = input()
Sc = input()

b = Sb
c = Sc
s = Sa[0]
a = Sa[1:]

for i in range(len(Sa)+len(Sb)+len(Sc)):
    if s == "a":
        if len(a) == 0:
            print("A")
            break
        s = a[0]
        a = a[1:]
    elif s == "b":
        if len(b) == 0:
            print("B")
            break
        s = b[0]
        b = b[1:]
    elif s == "c":
        if len(c) == 0:
            print("C")
            break
        s = c[0]
        c = c[1:]