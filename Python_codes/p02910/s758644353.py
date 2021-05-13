s = input().rstrip()
for i,l in enumerate(s):
    if i&1:
        if 'R' in l:
            print('No')
            break
    else:
        if 'L' in l:
            print('No')
            break
else:
    print('Yes')