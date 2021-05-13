s = input()

if s[0]  == 'A' and s[2:-1].count('C') == 1:
    for n in s[1:]:
        if n.islower():
            continue
        else:
            if n == 'C':
                continue
            else:
                print('WA')
                exit()
else:
    print('WA')
    exit()
print('AC')