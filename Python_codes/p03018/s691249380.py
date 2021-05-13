s=list(input())
n=len(s)
l=[]
i=0
while i<n:
    if i<n-1 and s[i]=='B' and s[i+1]=='C':
        l.append('D')
        i+=2
    else:
        l.append(s[i])
        i+=1
n=len(l)
ans=0
r=[0]*(n+1)
f=0
for i in range(n-1,-1,-1):
    if l[i]=='D':
        f+=1
    elif l[i]=='A':
        ans+=f
    else:
        f=0
print(ans)
