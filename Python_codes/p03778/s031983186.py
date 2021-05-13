w, a, b = map(int, input().split())

dist = abs(b - a)
if dist <= w:
    print(0)
else:
    print(dist - w)
