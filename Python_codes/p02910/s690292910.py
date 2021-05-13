s=input()
for i in range(len(s)):
    if i%2==0:
        if s[i] in 'RUD':
            continue
        else:
            print('No')
            break
    else:
        if s[i] in 'LUD':
            continue
        else:
            print('No')
            break
else:
    print('Yes')