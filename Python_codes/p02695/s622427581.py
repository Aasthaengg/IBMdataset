import sys
import itertools

N, M, Q = map(int, input().split())
abcd = []
z = [x for x in range(1,M+1)]
s = 0
d = 0
for i in range(Q):
    abcd.append(list(map(int, input().split())))

for A in itertools.combinations_with_replacement(z, N):
    d = 0
    for y in abcd:
        if A[y[1]-1] - A[y[0]-1] == y[2]:
            d += y[3]
    s = max(d, s)

print(s)