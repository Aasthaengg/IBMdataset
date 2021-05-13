s = input()
kw = 'keyence'

for i in range(8):
    if s[0:i] == kw[0:i] and s[-7 + i:] == kw[i:]:
        print('YES')
        break
else:
    print('NO')