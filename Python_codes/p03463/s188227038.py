N, A, B = tuple(map(int, input().split()))
i = 0
while True:
    if i % 2 == 0:
        if A + 1 != B:
            A += 1
        else:
            A -= 1
    else:
        if B - 1 != A:
            B -= 1
        else:
            B += 1
    if A < 1:
        print("Borys")
        break
    if B > N:
        print("Alice")
        break
    i += 1
