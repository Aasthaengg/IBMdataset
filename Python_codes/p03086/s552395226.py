S=list(input())
n=len(S)
ans=0
ansl=[0]
for i in range(n):
    if S[i]=="A" or S[i]=="C" or S[i]=="G" or S[i]=="T":
        ans+=1
    else:
        ans=0
    ansl.append(ans)
ansl.sort(key=int)
print(ansl[n])