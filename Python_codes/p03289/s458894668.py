s = str(input())
if s[0] == 'A' and s[2:len(s)-1].count('C') == 1:
    j = s.index('C')
    w = s[1:j] + s[j+1:]
    if w.lower() == w:
        print('AC')
    else:
        print('WA')
else:
    print('WA')