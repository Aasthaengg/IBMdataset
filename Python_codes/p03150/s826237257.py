S = input()

s = S.replace('keyence', '0')
lst = []
k = 'keyence'
jdg = False

if s[0] == '0' or s[-1] == '0':
    jdg = True
elif '0' in s:
    jdg = False
else:
    for i in range(1, len(k)):
        lst.append([k[:i], k[i:]])

    for i, j in enumerate(lst, start=1):
        if s[:i] == j[0] and s[i-7:] == j[1]:
            jdg = True
            break
if jdg: print('YES')
else: print('NO')
