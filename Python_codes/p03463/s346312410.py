n, a, b = map(int, input().split())

if abs(b - a) % 2 == 0:
    print("Alice")
elif abs(b - a) % 2 == 1:
    print("Borys")