S=list(input())
S=['_']+S
i=1
ans=0
while i<=len(S)-3:
    ans+=1
    if S[i-1]==S[i]:
        S[i+1]='_'
        i+=1
    i+=1

if len(S)==2:
    ans+=1
elif len(S)-i==1:
    ans+=1
elif S[i-1]!=S[i] and S[i]!=S[i+1]:
    ans+=2
else:
    ans+=1

print(ans)