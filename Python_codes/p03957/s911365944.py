s = input()
f = 0
for c in s:
    if f == 0 and c == 'C':
        f = 1
    elif f == 1 and c == 'F':
        f = 2
        break
if f == 2:
    print('Yes')
else:
    print('No')