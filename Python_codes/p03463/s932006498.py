N, A, B = [int(x) for x in input().split()]
if abs(B - A) % 2 == 0:
    print("Alice")
else:
    print("Borys")