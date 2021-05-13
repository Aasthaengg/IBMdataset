n, a, b = map(int, input().split())
while 1:
    if b != a+1:
        a += 1
    elif a != 1:
        a -= 1
    else:
        print("Borys")
        exit()
    if a != b-1:
        b -= 1
    elif b != n:
        b += 1
    else:
        print("Alice")
        exit()
