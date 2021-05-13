S = input()

A = list('AKIHABARA')
ap = [0, 4, 6, 8]
l = []

for i in range(2 ** 4):
    for j in range(4):
        if i >> j & 1 == 1:
            A[ap[j]] = ''
    l.append(''.join(A))
    A = list('AKIHABARA')

if S in l:
    print('YES')
else:
    print('NO')
