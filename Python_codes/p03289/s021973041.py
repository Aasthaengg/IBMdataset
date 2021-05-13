s = input()

if s[0] == 'A' and s[2:-1].count('C') == 1:
    for i in s:
        if i.islower() == True:
            continue
        elif i == 'A' or i == 'C':
            continue
        else:
            print('WA')
            exit()
else:
    print('WA')
    exit()

print('AC')