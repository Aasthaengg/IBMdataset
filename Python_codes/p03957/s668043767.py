s = input()

if 'C' in s and 'F' in s:
    if 'F' in s[s.index('C'):]:
        print('Yes')
        exit()
print('No')