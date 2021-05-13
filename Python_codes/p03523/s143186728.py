s = input()
a = 'AKIHABARA'
a = list(a)
idxs = [0, 4, 6, 8]
for i in range(2**4):
    for j in range(4):
        a[idxs[j]] = 'A' if i>>j&1 else ''
        if s==''.join(a):
            print('YES')
            exit(0)
print('NO')