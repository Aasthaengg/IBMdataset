S=input()
N=len(S)
i=0
now=0
ans=0
while i<N:
    if S[i]=='A':
        now+=1
    elif S[i:i+2]=='BC':
        ans+=now
        i+=1
    else:
        now=0
    i+=1
print(ans)