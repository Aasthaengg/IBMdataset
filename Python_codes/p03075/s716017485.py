import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

for v in itertools.combinations([a, b, c, d, e], 2):
    if v[1]-v[0] > k:
        print(':(')
        exit()
print('Yay!')
