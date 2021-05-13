from fractions import Fraction
from itertools import product

A, B, C, D, E, F = map(int, input().split(' '))

a_max = F // (A * 100)
b_max = F // (B * 100)

waters = set()

for a, b in product(range(0, a_max + 1), range(0, b_max + 1)):
    w = (a * A + b * B) * 100
    if w > F:
        continue

    waters.add(w)

waters = sorted(waters)[1:]
sugars = []

for w in sorted(waters):
    f1 = F - w
    f2 = w // 100 * E
    c_max = min(f1 // C, f2 // C)
    d_max = min(f1 // D, f2 // D)

    max_sugar = 0

    for c, d in product(range(0, c_max + 1), range(0, d_max + 1)):
        s = C * c + D * d
        if s > f1 or s > f2:
            continue
        max_sugar = max(max_sugar, s)

    sugars.append(max_sugar)

dense = [Fraction(s, s + w) for w, s in zip(waters, sugars)]

max_dense = 0
index = -1
for i, d in enumerate(dense):
    if d > max_dense:
        max_dense = d
        index = i

if index == -1:
    print(A * 100, 0)
else:
    print(waters[index] + sugars[index], sugars[index])
