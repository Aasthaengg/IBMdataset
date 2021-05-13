S=input()
if 'C' in S and 'F' in S:
    l=S.index('C')
    r=-1
    for i in reversed(range(len(S))):
        if S[i]=='F':
            r=i
            break
    if r==-1 or l>=r:
        print('No')
    else:
        print('Yes')
else:
    print('No')