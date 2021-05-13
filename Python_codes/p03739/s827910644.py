from itertools import accumulate
n, *A = map(int, open(0).read().split())
B = list(accumulate(A))
p0 = n0 = p1 = n1 = 0
for i, b in enumerate(B):
    if i % 2 == 0:
        if b+p0-n0 <= 0:
            p0 += abs(b+p0-n0)+1
        if b+p1-n1 >= 0:
            n1 += abs(b+p1-n1)+1
    else:
        if b+p0-n0 >= 0:
            n0 += abs(b+p0-n0)+1
        if b+p1-n1 <= 0:
            p1 += abs(b+p1-n1)+1
print(min(p0+n0, p1+n1))
