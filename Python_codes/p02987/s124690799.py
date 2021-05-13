S = input()
SetS = list(set(S))
if len(SetS)==2 and S.count(SetS[0])==S.count(SetS[1]):
    print('Yes')
else:
    print('No')