s=list(input())
t=list(input())
match=[]
accord=[]
for i in range(len(s)):
    if s[i] in match:
        ind=match.index(s[i])
        acc=accord[ind]
        if t[i]!=acc:
            print('No')
            exit()
    elif t[i] in accord:
        ind=accord.index(t[i])
        mat=match[ind]
        if s[i]!=mat:
            print('No')
            exit()
    else:
        match.append(s[i])
        accord.append(t[i])
print('Yes')