S = list(input())
set_S = list(set(S))
if(len(set_S)==2):
    if((S.count(set_S[0])==2) and (S.count(set_S[1])==2)):
        print('Yes')
    else:
        print('No')
else:
    print('No')