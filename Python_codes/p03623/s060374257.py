x, a, b = map(int, input().split())

xa = abs(x - a)
xb = abs(x - b)

if xa > xb:
    print("B")
else:
    print("A")