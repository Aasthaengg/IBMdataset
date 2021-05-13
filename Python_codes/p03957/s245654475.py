s = input()
if 'C' in s:
    d = s.find('C')
    if 'F' in s[d:]:
        print('Yes')
        exit(0)
print('No')