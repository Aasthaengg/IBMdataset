S=input()
x=set(['A','T','C','G'])
ans=0
l=len(S)
for i in range(l+1):
    for j in range(i,l+1):
        #print(i,j,S[i:j])
        for s in S[i:j]:
            if s not in x:
                break
        else:
            ans=max(ans,j-i)
print(ans)