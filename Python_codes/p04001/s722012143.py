s=input()
ans=0
for i in range(1 << len(s)-1):
    l=[]
    for j in range(len(s)-1):
        if (i>>j)&1==1:
            l.append(s[j])
            l.append("+")
        else:
            l.append(s[j])
    l.append(s[len(s)-1])
    ans+=eval(''.join(l))
print(ans)