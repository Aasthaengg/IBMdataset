S = input()

if S[0] == 'A' and S[2:-1].count('C') == 1: 
    s = S.replace('A', 'a').replace('C', 'c')
    t = s.lower()
    if s == t:
        print('AC')
        exit()
print('WA')