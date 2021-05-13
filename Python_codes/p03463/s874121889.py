n, a, b = map(int, input().split())

if a == 1 and b == 2 or (b - a) % 2:
    print("Borys")
else:
    print("Alice")
