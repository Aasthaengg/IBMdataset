from math import ceil
s=list(input())
n=len(s)
l=[]
m=[]
buf=[]
for i in range(n):
    if s[i]!="x":
        l.append(s[i])
m=l[::-1]
#print(l,m)
left=[]
right=[]
ans=0
if m==l:
    flag=1
    for i in range(ceil(len(l)/2)):
        buf.append(l[i])
    piv=0
    cnt=0
    #print(buf)
    for i in range(n):
        if piv==len(buf):
            break
        if s[i]==buf[piv]:
            left.append(cnt)
            cnt=0
            piv=piv+1
        else:
            cnt=cnt+1
    piv=0
    cnt=0
    for i in range(n-1,-1,-1):
        if piv==len(buf):
            break
        if s[i]==buf[piv]:
            right.append(cnt)
            cnt=0
            piv=piv+1
        else:
            cnt=cnt+1
    #print(left,right)
    for i in range(len(left)):
        ans=ans+abs(left[i]-right[i])
    print(ans)
else:
    print("-1")
