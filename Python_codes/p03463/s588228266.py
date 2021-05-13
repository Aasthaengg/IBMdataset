n, a, b = map(int, input().split())

if n == 2:
    print("Borys")
elif (b - a) % 2 == 0:
    print("Alice")
elif (b - a) % 2 == 1:
    print("Borys")
