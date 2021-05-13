s = input()
ok = True
ss = ''
# print(s[2:-1])
if s[0] == 'A': 
    if 'C' in s[2:-1]:
        for i in range(len(s)):
            if s[i].isupper():
                ss += s[i]
        if ss == 'AC':
            pass
        else:
            ok = False
    else:
        ok = False
else:
    ok = False

if ok:
    print('AC')
else:
    print('WA')