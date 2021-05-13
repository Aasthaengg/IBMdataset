(n, m, l) = [int(i) for i in input().split()]

A = []
for nc in range(n):
    A.append([int(i) for i in input().split()])

B = []
for mc in range(m):
    B.append([int(i) for i in input().split()])

product = [[0 for d in range(l)] for dd in range(n)]

for nc in range(n):
    for lc in range(l):
        for mc in range(m):
            product[nc][lc] += A[nc][mc] * B[mc][lc]

for r in product:
    print(' '.join([str(d) for d in r]))