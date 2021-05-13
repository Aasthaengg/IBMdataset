s=str(input())
n=len(s)
z=0
ans=0
i=0
while i<=n-2:
    if s[i]=='A':
        z+=1
        i+=1
        continue
    elif s[i:i+2]=='BC' and z>0:
        ans+=z
        i+=2
    else:
        z=0
        i+=1
print(ans)