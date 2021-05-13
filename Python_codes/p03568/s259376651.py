from itertools import product

N = int(input())
A = [int(a) for a in input().split()]

count = 0
for diffs in product((-1, 0, 1), repeat=N):
    for a, d in zip(A, diffs):
        if (a % 2 == 0 and d == 0) or (a % 2 == 1 and d != 0):
            count += 1
            break

print(count)