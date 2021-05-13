a, b, c, d = map(int, input().split())

ac = a * c
ad = a * d
bc = b * c
bd = b * d

sorted = sorted([ac, ad, bc, bd])
print(sorted[3])