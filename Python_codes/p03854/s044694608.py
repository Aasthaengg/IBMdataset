s = input()

s = s[::-1]
lis = ['dreamer', 'dream', 'eraser', 'erase']
nlis = []
for i in lis:
    nlis.append(i[::-1])


for i in range(10**5 + 1):
    for j in nlis:
        if s.startswith(j):
            s = s[len(j):]


if s == '':
    print('YES')
else:
    print('NO')