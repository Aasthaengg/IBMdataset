from itertools import combinations as C

d = {}
for _ in range(int(input())):
    s = input()[0]
    if s in "MARCH":
        d[s] = d.get(s, 0) + 1
else:
    print(sum([p * q * r for p, q, r in C(d.values(), 3)]))