s = input()
if s[0] == 'A' and s[2:-1].count('C') == 1 and s[1].islower() == True and s[-1].islower() == True: print('AC')
else: print('WA')