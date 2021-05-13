n, a, b = [int(x) for x in input().split()]

dist = b-a
if dist % 2:
    print("Borys")
else:
    print("Alice")