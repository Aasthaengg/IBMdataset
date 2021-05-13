s = list(input())
if s[0] != 'A':
    print('WA')
elif s[2:-1].count('C') != 1:
    print('WA')
else:
    i = s.index('C')
    s.pop(i)
    s.pop(0)
    s = ''.join(s)
    if s.islower():
        print('AC')
    else:
        print('WA')