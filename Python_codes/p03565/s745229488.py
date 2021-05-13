S=input()
T=input()
ns=len(S)
nt=len(T)
ans=[]
i=0
while i+nt<=ns:
    j=0
    while j<nt:
        if S[i+j]=='?' or S[i+j]==T[j]:
            j+=1
        else:
            break
    if j==nt:
        A=S[:i]+T+S[i+nt:]
        A=A.replace('?','a')
        ans.append(A)
    i+=1
    
if ans:
    print(sorted(ans)[0])
else:
    print('UNRESTORABLE')