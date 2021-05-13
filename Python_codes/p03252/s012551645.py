s=list(input())
t=list(input())
S={}
T={}
for i in s:
    if i in S.keys():
        S[i]+=1
    else:
        S[i]=1
for i in t:
    if i in T.keys():
        T[i]+=1
    else:
        T[i]=1
Svalues=sorted(S.values())
Tvalues=sorted(T.values())
if Tvalues==Svalues:
    print('Yes')
else:
    print('No')