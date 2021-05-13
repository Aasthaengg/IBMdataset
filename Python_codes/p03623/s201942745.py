x, a, b = map(int, input().split())
da = abs(x-a)
db = abs(x-b)
print("A" if da < db else "B")