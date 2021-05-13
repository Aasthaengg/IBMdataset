S = input()
CFlag = False
FFlag = False
for T in S:
    if T=='C':
        CFlag = True
    if CFlag and T=='F':
        FFlag = True
        break
if FFlag:
    print('Yes')
else:
    print('No')