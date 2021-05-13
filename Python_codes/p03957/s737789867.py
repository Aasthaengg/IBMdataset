s = input()
if 'C' in s and 'F' in s[s.index('C')+1:]:
    print('Yes')
    exit()
else:
    print('No')