from itertools import groupby

n, k = map(int, input().split())

D = {
    'L': 0,
    'R': 0
}

for val, it in groupby(input()):
    D[val] += 1

u = max([1, D['L'] + D['R'] - 2 * k])

print(n - u)
