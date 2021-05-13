s=list(input())
if len(set(s))==1 and s[0]=='x':
    print(0)
    exit()

n=len(s)

nox=[i for i in s if i!='x']
if nox!=nox[::-1]:
    print(-1)
    exit()

ans=0
i=0
j=n-1
while i<j:
    if s[i]==s[j]:
        i+=1
        j-=1
    elif s[i]=='x':
        i+=1
        ans+=1
    elif s[j]=='x':
        j-=1
        ans+=1
print(ans)