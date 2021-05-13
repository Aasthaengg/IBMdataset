Sa = list(input())
Sb = list(input())
Sc = list(input())

a = "a"

while True:
    if a == "a":
        if len(Sa) == 0:
            print("A")
            break
        a = Sa[0]
        Sa.pop(0)
    if a == "b":
        if len(Sb) == 0:
            print("B")
            break
        a = Sb[0]
        Sb.pop(0)
    if a == "c":
        if len(Sc) == 0:
            print("C")
            break
        a = Sc[0]
        Sc.pop(0)
