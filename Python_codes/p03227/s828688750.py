S=str(input())
ans=''
for i in range(len(S)):
    if len(S)==2:
        ans+=S[i]
    else:
        ans+=S[-1-i]
print(ans)