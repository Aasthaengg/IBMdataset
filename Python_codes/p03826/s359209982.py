a, b, c, d = tuple(map(int, input().split()))
areaA = a * b
areaB = c * d
if areaA > areaB:
    print(areaA)
else:
    print(areaB)
