S = input()

cpos = -1
# fpos = 0
ans = False

for i, si in enumerate(S):
    if si == 'C':
        cpos = i
        break

if cpos >= 0:
    fpos = -1
    for i, si in enumerate(S):
        if si == 'F':
            fpos  = i
    if fpos > cpos:
        print('Yes')
    else:
        print('No')
else:
    print('No')