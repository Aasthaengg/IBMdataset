import itertools
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
l = [a, b, c, d, e]
for v in itertools.combinations(l, 2):
    if abs(v[0]-v[1]) > k:
        print(':(')
        exit()
print('Yay!')
