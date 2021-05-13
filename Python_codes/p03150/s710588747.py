import re
S = input()
k = 'keyence'
for i in range(0, len(k)+1):
    rs = '^' + k[:i] + '.*' + k[i:] + '$'
    if re.match(rs, S) is not None:
        print('YES')
        break
else:
    print('NO')

