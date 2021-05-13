n, a, b = map(int, input().split(" "))
if a > b:
    diff = a - b - 1
else:
    diff = b - a - 1

if diff % 2 == 0:
    print("Borys")
else:
    print("Alice")