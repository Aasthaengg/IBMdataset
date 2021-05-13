a, b, c, d, e, f = map(int, input().split())
a *= 100
b *= 100

W = []
for i in range(f+1):
    for j in range(f+1):
        w = a*i + b*j
        if w <= f and w > 0:
            W.append(w)
S = []
for i in range(f+1):
    for j in range(f+1):
        s = c*i + d*j
        if s <= f:
            S.append(s)

cmax = -1
solubility = e/(e+100)
argmax = 0, 0

for w in W:
    for s in S:
        if w+s > f:
            continue

        concentration = s/(w+s)

        if cmax < concentration <= solubility:
            cmax = s/(w+s)
            argmax = w+s, s

print(*argmax)
