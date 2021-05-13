s = input()
w = 0
for i in range(len(s)):
    if s[i] == 'o':
        w += 1

w += 15 - len(s)
if 8 <= w:
    print('YES')
else:
    print('NO')
