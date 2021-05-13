n, a, b = map(int, input().split())
d = b - a - 1
print("Alice") if d % 2 else print("Borys")