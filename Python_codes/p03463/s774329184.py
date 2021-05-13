N, A, B = map(int, input().split())
t_a = True
t_b = False
while True:
    if t_a:
        if A - B > 0:
            if A - 1 == B:
                A += 1
            else:
                A -= 1
        elif A - B < 0:
            if A + 1 == B:
                A -= 1
            else:
                A += 1

        if A == B or A < 0 or A > N:
            print("Borys")
            break
        t_a = False
        t_b = True
    elif t_b:
        if B - A > 0:
            if B - 1 == B:
                B += 1
            else:
                B -= 1
        elif B - A < 0:
            if B + 1 == B:
                B -= 1
            else:
                B += 1

        if A == B or B < 0 or B > N:
            print("Alice")
            break
        t_a = True
        t_b = False