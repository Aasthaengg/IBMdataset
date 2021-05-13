n = int(input())
s = input()

rc, bc = 0, 0
for i in s:
    if i == 'R':
        rc += 1
    else:
        bc += 1
if rc > bc:
    print('Yes')
else:
    print('No')