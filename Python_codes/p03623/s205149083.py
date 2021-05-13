x, a, b = map(int, input().split())

print("A" if (x - a) ** 2 < (x - b) ** 2 else "B")