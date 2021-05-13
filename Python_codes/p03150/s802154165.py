k = list('keyence')
s = list(input())
while len(k) > 0:
    if k[0] == s[0]:
        k.pop(0)
        s.pop(0)
    else:
        break
while len(k) > 0:
    if k[-1] == s[-1]:
        k.pop()
        s.pop()
    else:
        break
if len(k) == 0:
    print('YES')
else:
    print('NO')