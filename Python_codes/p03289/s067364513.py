s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1:
    for i in range(1,len(s)):
        if s[i].islower() == True:
            continue
        else:
            if s[i] == 'C':
                continue
            else:
                print('WA')
                exit()
else:
    print('WA')
    exit()
print('AC')