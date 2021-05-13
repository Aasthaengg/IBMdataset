s = input()
w = 0
for item in s:
    if item == 'o':
        w += 1

w += 15 - len(s)
if 8 <= w:
    print('YES')
else:
    print('NO')
