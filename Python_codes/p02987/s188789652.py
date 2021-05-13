s = input()
S = list(set(s))

if s.count(S[0]) == 2 and s.count(S[1]) == 2:
    print('Yes')
else:
    print('No')