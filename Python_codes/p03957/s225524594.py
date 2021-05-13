s = input()
if s.count('C') > 0 and s[s.find('C'):].count('F') > 0:
    print('Yes')
else:
    print('No')