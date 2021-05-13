import sys
from itertools import combinations

input = sys.stdin.readline
d = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for i in range(int(input())):
    a = input()
    if a[0] in "MARCH":
        d[a[0]] += 1

l = [i for i in d.values() if i != 0]
print(sum(i * j * k for i, j, k in combinations(l, 3)))
