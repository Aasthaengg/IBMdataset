import random


d=int(input())
C=[int(i) for i in input().split()]
s=[[int(i) for i in input().split()] for q in range(d)]

sco=0
L=[0 for i in range(26)]
ans=[]

#calc
for i in range(d):
    mayou=0
    est=s[i][0]+C[0]*(i+1-L[0])
    for p in range(1,26):
        if s[i][p]+C[p]*(i+1-L[p]) > est:
            mayou=p
            est=s[i][p]+C[p]*(i+1-L[p])
    ans.append(mayou)
    L[mayou]=i+1


sco=est

##以下表示
"""
L=[0 for i in range(26)]
for q in range(d):
    t=ans[q]
    sco+=s[q][t]
    
    
    L[t]=q+1
    for i in range(26):
        if L[i]!=-1:
            sco-=C[i]*(q+1-L[i])
    
    print(sco)
"""


m=1000000

for que in range(m):
    newsco=sco
    dn,q=random.choice(range(1,d)),random.choice(range(1,27))
    dn-=1
    q-=1
    old=ans[dn]
    ans[dn]=q
    now=dn
    cnt=1
    while now!=0 and ans[now]!=old:
        now-=1
        cnt+=1
    now=dn
    while now!=d and ans[now]!=old:
        newsco-=cnt*C[old]
        now+=1
        cnt+=1
    newsco-=s[dn][old]
    newsco+=s[dn][q]
    now=dn
    cnt=1
    while now!=0 and ans[now]!=q:
        now-=1
        cnt+=1
    now=dn
    while now!=d and ans[now]!=q:
        newsco+=cnt*C[q]
        now+=1
        cnt+=1
    #print(newsco)
    if newsco>sco:
        sco=newsco
        #print(newsco)
    else:
        ans[dn]=old

for ele in ans:
    print(ele+1)
    
