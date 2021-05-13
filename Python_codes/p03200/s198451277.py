S=list(str(input()))
ans=0
sofar=0
for i in range(len(S)):
    if S[i]=='W':
        ans+=i-sofar
        sofar+=1
print(ans)