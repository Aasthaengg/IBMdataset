s=input()
ans=1000
import string
ss=string.ascii_lowercase
for c in list(ss):
    temp=s
    p=0
    nex=""
    while len(set(list(temp)))!=1:
        for i in range(len(temp)-1):
            if c in (temp[i],temp[i+1]):
                nex+=c
            else:nex+=temp[i]
        p+=1
        temp=nex
        nex=""
    ans=min(p,ans)
print(ans)