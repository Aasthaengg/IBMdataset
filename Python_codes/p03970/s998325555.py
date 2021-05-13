S=list(input())
L=list("CODEFESTIVAL2016")
ans=0
for i in range(16):
    if(S[i]!=L[i]):
        ans+=1
print(ans)
