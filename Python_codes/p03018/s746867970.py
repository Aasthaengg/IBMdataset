s=input().replace('BC','D')
a=[]
b=''
for c in s:
    if c=='B' or c=='C':
        a.append(b)
        b=''
    else:
        b+=c
a.append(b)
ans=0
for i in a:
    ac=0
    for j in i:
        if j=='A':
            ac+=1
        else:
            ans+=ac
print(ans)