N, A, B = map(int, input().split())
t_a = True
t_b = False
while True:
    if t_a:
        if A - 1 == B or A - B <= -1:
            A += 1
        elif A + 1 == B or A - B >= 1:
            A -= 1

        if A == B or A < 0 or A > N:
            print("Borys")
            break
        t_a = False
        t_b = True
    elif t_b:
        if B - 1 == B or B - A <= -1:
            B += 1
        elif B + 1 == B or B - A >= 1:
            B -= 1

        if A == B or B < 0 or B > N:
            print("Alice")
            break
        t_a = True
        t_b = False