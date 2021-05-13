s = list(input())
ac, bc, cc = 0, 0, 0
for i in range(len(s)):
    if s[i] == 'a':
        ac += 1
    elif s[i] == 'b':
        bc += 1
    else:
        cc += 1
if abs(ac-bc) > 1 or abs(ac-cc) > 1 or abs(bc-cc) > 1:
    print('NO')
else:
    print('YES')