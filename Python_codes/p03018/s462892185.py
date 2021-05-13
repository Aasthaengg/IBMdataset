s=input().replace('BC','D')
ans=0
ac=0
for c in s:
    if c=='A':
        ac+=1
    elif c=='D':
        ans+=ac
    else:
        ac=0
print(ans)