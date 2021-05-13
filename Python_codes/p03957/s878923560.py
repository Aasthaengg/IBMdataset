s = input()
if s.find('C') >= 0 and s.find('F') >= 0:
    if s.index('C') < s.rindex('F'):
        print('Yes')
    else:
        print('No')
else:
    print('No')
