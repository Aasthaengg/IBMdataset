S = input()
s = list(set(S))
if(len(s) == 2):
    if(S.count(s[0]) == 2 and S.count(s[1]) == 2):
        print('Yes')
    else:
        print('No')
else:
    print('No')
