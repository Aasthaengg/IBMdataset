S=list(str(input()))
a=[]
for i in range(len(S)):
    if (i+1)%2==0 and (S[i]=='L' or S[i]=='U' or S[i]=='D'):
        a.append('Yes')
    elif (i+1)%2==1 and (S[i]=='R' or S[i]=='U' or S[i]=='D'):
        a.append('Yes')
    else:
        a.append('No')
if 'No' in a:
    print('No')
else:
    print('Yes')