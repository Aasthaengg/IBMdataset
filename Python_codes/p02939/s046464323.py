S=input()
tmp=S[0]
i=1
ans=1
while i<len(S)-1:
    # print(S[i],tmp)
    if S[i]!=tmp:
        ans+=1
        tmp=S[i]
        i+=1
    else:
        ans+=1
        tmp=S[i:i+2]
        i+=2
if i>=len(S):
    print(ans)
elif tmp==S[i]:
    print(ans)
else:
    print(ans+1)
