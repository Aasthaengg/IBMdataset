A, B = map(int, input().split())
G1 = [['#'] * 100 for i in range(50)]
G2 = [['.'] * 100 for i in range(50)]

A, B = A - 1, B - 1

h, w = 0, 0
for a in range(A):
    if w > 99:
        h += 2
        w = 0
    G1[h][w] = '.'
    w += 2

h, w = 1, 0
for b in range(B):
    if w > 99:
        h += 2
        w = 0
    G2[h][w] = '#'
    w += 2


print(100, 100)
for g in G1:
    print(''.join(g))
for g in G2:
    print(''.join(g))
