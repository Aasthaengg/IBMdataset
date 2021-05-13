def rep(s):
    a,b='',[]
    for i in range(len(s)):
        if s[i]=='C' or s[i]=='B':
            b.append(a)
            a=''
        else:
            a+=s[i]
    b.append(a)
    a=[]
    for i in range(len(b)):
        if b[i]!='':
            a.append(b[i])
    return a
s=rep(input().replace('BC','D'))
b=0
for i in s:
    a=0
    for j in i:
        if j=='A':
            a+=1
        else:
            b+=a
print(b)