from collections import deque
X=input()
N=len(X)
cnt=0
sptm=0
ans=0
d=deque()
"""
for i in range(N):
    if X[i]=="S":
        sptm=sptm+1
    if X[i]=="T":
        sptm=sptm-1
    if sptm<0:
        ans=ans+1
        sptm=0
    #print(sptm,ans)
print(ans+max(0,sptm))
"""
for i in range(N):
    d.append(X[i])
    if len(d)>1:
        s1=d.pop()
        s2=d.pop()
        if (s2!="S")or(s1!="T"):
            d.append(s2)
            d.append(s1)
    #print(d)
print(len(d))