import itertools
*l, k = [int(input()) for _ in range(6)]

c = itertools.combinations(l, 2)

for x, y in c:
    if abs(x-y) > k:
        print(':(')
        exit()

print('Yay!')