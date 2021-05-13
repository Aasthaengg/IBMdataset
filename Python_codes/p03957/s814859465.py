s = input()
C = False
F = False

for i in s:
    if i == 'C':
        C = True
    elif i == 'F' and C:
        F = True

if C and F:
    print('Yes')
else:
    print('No')