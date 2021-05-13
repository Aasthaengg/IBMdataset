from math import ceil

s = sorted(input())
l = ceil(len(s)/2)

hands = (['g'] * l) + (['p'] * l)

c = 0

for x, y in zip(s, hands):
    if x != y:
        c += 1

print(c)