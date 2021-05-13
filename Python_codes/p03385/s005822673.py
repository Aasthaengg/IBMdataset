n = input()
acount = 0
bcount = 0
ccount = 0
for s in n:
    if s == 'a':
        acount+=1
    if s == 'b':
        bcount+=1
    if s == 'c':
        ccount+=1
if acount == 1 & bcount == 1 & ccount == 1:
    print('Yes')
else:
    print('No')