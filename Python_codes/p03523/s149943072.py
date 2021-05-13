S=list(str(input()))
for i in range(9):
    S.append('')
t=''
for i in range(9):
    if i==0 or i==4 or i==6 or i==8:
        if S[0]=='A':
            t+=S.pop(0)
        else:
            t+='A'
    elif i==1:
        if S[0]=='K':
            t+=S.pop(0)
    elif i==2:
        if S[0]=='I':
            t+=S.pop(0)
    elif i==3:
        if S[0]=='H':
            t+=S.pop(0)
    elif i==5:
        if S[0]=='B':
            t+=S.pop(0)
    elif i==7:
        if S[0]=='R':
            t+=S.pop(0)
if t=='AKIHABARA' and len(S)==9:
    print('YES')
else:
    print('NO')
