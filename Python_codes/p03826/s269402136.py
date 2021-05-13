a, b, c, d = map(int, input().split())

ab = a * b
cd = c * d

if ab >= cd:
    print(ab)
elif ab < cd:
    print(cd)