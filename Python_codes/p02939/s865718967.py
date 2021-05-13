S=input()
idx=0
ans=len(S)
s=""
while(idx<len(S)):
    if s==S[idx]:
        ans-=1
        s=""
        idx+=2
    else:
        s=S[idx]
        idx+=1
print(ans)