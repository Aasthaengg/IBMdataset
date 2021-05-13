n,k=map(int,input().split())
s=input()
s+="6"
c=0
l=[]
zcnt=0
for i in range(n):
  if s[i]!=s[i+1]:
    if s[i]=="0":zcnt+=1
    l.append((s[i],i+1-c))
    c=i+1
L=len(l)
sl=[0]*(L+1)
for i in range(L):
    sl[i+1]=sl[i]+l[i][1]
if k>=zcnt:print(n);exit()
ans=0
if s[0]=="0":
    for i in range(zcnt-k+1):
        ans=max(ans,sl[min(L,2*k+i*2)]-sl[max(0,i*2-1)])
    print(ans)
else:
    for i in range(zcnt-k+1):
        ans=max(ans,sl[min(L,2*k+i*2+1)]-sl[i*2])
    print(ans)