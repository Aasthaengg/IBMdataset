S1=input()
S2='CODEFESTIVAL2016'

ans=0
for i in range(len(S1)):
    if S1[i]!=S2[i]:
        ans+=1

print(ans)