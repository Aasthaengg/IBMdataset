from itertools import product

n = int(input())
A = tuple(map(int, input().split(' ')))
q = int(input())
M = tuple(map(int, input().split(' ')))

numbers = set()
for bits in product((0, 1), repeat=n):
    numbers.add(sum([a * b for a, b in zip(A, bits)]))

for m in M:
    if m in numbers:
        print('yes')
    else:
        print('no')

