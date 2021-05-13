s = str(input())
C = 0
F = 0
for i in s:
    if C == 0 and i == 'C':
        C = 1
    elif C == 1 and i == 'F':
        F = 1
if F == 1:
    print('Yes')
else:
    print('No')