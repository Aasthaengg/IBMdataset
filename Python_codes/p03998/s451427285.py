A = list(input())
B = list(input())
C = list(input())

tmp = A.pop(0)

for _ in range(500):
    if tmp == "a":
        if not A:
            print("A")
            exit(0)
        tmp = A.pop(0)
    elif tmp == "b":
        if not B:
            print("B")
            exit(0)
        tmp = B.pop(0)
    else:
        if not C:
            print("C")
            exit(0)
        tmp = C.pop(0)