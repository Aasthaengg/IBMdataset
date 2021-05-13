s=input()
#左に>が続く個数、右に<が続く個数
l=[0]
r=[0]
l_,r_=0,0
for i in range(len(s)):
    if s[i]=='<':
        l_+=1
    else:
        l_=0
    l.append(l_)
    if s[-1-i]=='>':
        r_+=1
    else:
        r_=0
    r.append(r_)
r.reverse()
ans=0
for i in range(len(s)+1):
    ans+=max(l[i],r[i])
print(ans)
