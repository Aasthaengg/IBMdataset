S=list(input())
N=len(S)
ans=100

for s in S:
    i=0
    C=0
    count2=0
    while i<N:
        if s!=S[i]:
            count2+=1
        else:
            C=max(C,count2)
            count2=0
        i+=1
    C=max(C,count2)
    ans=min(C,ans)

print(ans)