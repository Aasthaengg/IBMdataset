s = list(input())
if s[0]=='A':
    s.remove(s[0]);   l = len(s)
    for i in range(l):
        if s[1:l-1].__contains__('C'):
            s.remove('C')
            print('AC' if str(s) == str(s).lower() else 'WA');   break
        else:
            print('WA');   break
else:
    print('WA')