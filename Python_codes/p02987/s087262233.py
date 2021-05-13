s = input()
chk = {}
for i in s:
    if i not in chk:
        chk[i] = 1
    else:
        chk[i] += 1

if len(chk) == 2 and chk[i] == 2:
    print('Yes')
else:
    print('No')