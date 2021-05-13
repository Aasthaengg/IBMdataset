S = input()

C = False
# F = False
ans = False
for si in S:
    if si == 'C':
        C = True
    if C and si == 'F':
        ans = True

if ans:
    print('Yes')
else:
    print('No')