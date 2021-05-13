n, a, b = map(int, input().rstrip("\n").split())

print("Borys" if (b - a) % 2 else "Alice")