x, a, b = [int(s) for s in input().split()]
print("A" if abs(x - a) < abs(x - b) else "B")