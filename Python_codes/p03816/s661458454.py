from collections import Counter

N, *A = map(int, open(0).read().split())

ctr = Counter(A)
c0 = 0
c1 = 0
for v in ctr.values():
    if v % 2 == 0:
        c0 += 1
    else:
        c1 += 1

print(c1 + c0 - c0 % 2)
