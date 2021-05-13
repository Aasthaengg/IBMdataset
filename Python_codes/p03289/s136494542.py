s = input()

if s[0] != 'A':
        print('WA')
        exit()

if s[2:-1].count('C') != 1:
        print('WA')
        exit()

s = s.replace('C',"")

if s[1:].islower():
        print('AC')
else:
        print('WA')