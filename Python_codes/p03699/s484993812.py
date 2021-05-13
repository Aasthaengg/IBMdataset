N,*S=map(int,open(0))
S.sort()

ans=sum(S)
i=0
if ans%10==0:
    while i<N:
        if S[i]%10>0:
            ans-=S[i]
            break
        i+=1

if i==N:
    print(0)
else:
    print(ans)