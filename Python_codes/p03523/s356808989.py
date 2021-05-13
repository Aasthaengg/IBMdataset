s = input()
l = [0, 4, 6, 8]
for i in range(16):
    st = list('AKIHABARA')
    for j in range(4):
        if (i >> j) & 1:
            st[l[j]] = ''
    if s == ''.join(st):
        print('YES')
        exit(0)
print('NO')