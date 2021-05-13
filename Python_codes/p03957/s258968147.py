S = input()

c, f = False, False
for s in S:
    if s == 'C':
        c = True
    if c and s == 'F':
        f = True
if c and f:
    print('Yes')
else:
    print('No')
