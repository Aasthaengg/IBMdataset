import itertools


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

combs = itertools.combinations([a, b, c, d, e], 2)

can_connects = [abs(x[0] - x[1]) <= k for x in combs]

if all(can_connects):
    print('Yay!')
else:
    print(':(')


