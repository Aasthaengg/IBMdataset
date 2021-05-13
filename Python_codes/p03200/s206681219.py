S=input()
W=0
ans=0
for i in range(len(S)):
    if S[i]=='W':
        W+=1
        ans+=i+1-W
print(ans)
