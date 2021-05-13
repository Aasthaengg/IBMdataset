S=input()
#変わり目数える
pre=S[0]
ans=0
for i in range(1,len(S)):
    s=S[i]
    if s!=pre:
        ans+=1
    pre=s
print(ans)