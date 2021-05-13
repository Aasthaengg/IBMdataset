s=input()

if 'C' in s and 'F' in s:
    if s.find('C') < s.rfind('F'):
        print('Yes')
    else:
        print('No')
else:
    print('No')