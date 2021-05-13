S = input()
l = []
pattern = [format(i, 'b').zfill(4) for i in range(2 ** 4)]

for i in pattern:
    tmp = list(map(int, list(i)))
    l.append('A' * tmp[0] + 'KIH' + 'A' * tmp[1] + 'B' + 'A' * tmp[2] + 'R' + 'A' * tmp[3])

if S in l:
    print('YES')
else:
    print('NO')