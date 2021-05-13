import sys
S = input()

if S[0] is 'A' and S[2:-1].count('C') == 1:
    if S[-1] != 'C' and S[:2].count('C') == 0:
        S = S.replace('C', '')
        S = S[1:]
        for i in S:
            if i.islower():
                continue
            else:
                print('WA')
                sys.exit()
        print('AC')
else:
    print('WA')    
