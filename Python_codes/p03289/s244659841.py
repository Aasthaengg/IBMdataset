s = input()
if s[0] == 'A' and s.count('A') == 1 and s.count('C') == 1 and s[2:-1].count('C') == 1:
    s = s.replace('A', '').replace('C', '')
    for c in s:
        if ord(c) < ord('a'):
            print('WA')
            exit(0)
    print('AC')
else:
    print('WA')
