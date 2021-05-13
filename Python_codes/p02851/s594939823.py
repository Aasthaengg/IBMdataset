import sys
input=sys.stdin.readline
n,k=map(int,input().split())
a=list(map(int,input().split()))
c1=[0]
c2=[k]
s=0
if k==1:
    print(0)
    sys.exit()
for i in range(n):
    s=(s+a[i])%k
    c1.append(s-i-1)
    c2.append(s+k-i-1)
d1={}
for i in range(1,n+1):
    if c1[i] in d1:
        d1[c1[i]]+=1
    else:
        d1[c1[i]]=1
ans=0
for i in range(n):
    if c1[i] in d1:
        ans+=d1[c1[i]]
    d1[c1[i+1]]-=1
d2={}
for i in range(1,min(k,n+1)):
    if c2[i] in d2:
        d2[c2[i]]+=1
    else:
        d2[c2[i]]=1
for i in range(n):
    if c1[i] in d2:
        ans+=d2[c1[i]]
    d2[c2[i+1]]-=1
    if i+k<=n:
        if c2[i+k] in d2:
            d2[c2[i+k]]+=1
        else:
            d2[c2[i+k]]=1
print(ans)








