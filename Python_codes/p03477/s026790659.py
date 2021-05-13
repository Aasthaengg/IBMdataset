# ABC 083: A – Libra
a, b, c, d = [int(s) for s in input().split()]
if a + b > c + d:
    print('Left')
elif a + b == c + d:
    print('Balanced')
else:
    print('Right')