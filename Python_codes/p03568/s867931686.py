from itertools import product
N = int(input())
A = list(map(int, input().split()))
r = 0
for pp in product((-1, 0, 1), repeat=N):
    s = 1
    for p, a in zip(pp, A):
        s *= a+p
    if s % 2 == 0:
        r += 1
print(r)
