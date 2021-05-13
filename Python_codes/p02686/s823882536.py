import sys
input=sys.stdin.readline
n=int(input())
sp=[]
sn=[]
for i in range(n):
    s=input().rstrip()
    m=0
    temp=0
    for j in s:
        if j=='(':
            temp+=1
        else:
            temp-=1
        m=min(m,temp)
    m=-m
    if temp>=0:
        sp.append((m,temp))
    else:
        sn.append((m+temp,-temp))
sp.sort()
sn.sort()
vp=0
for i in sp:
    if vp-i[0]<0:
        print('No')
        sys.exit()
    else:
        vp+=i[1]
vn=0
for i in sn:
    if vn-i[0]<0:
        print('No')
        sys.exit()
    else:
        vn+=i[1]
if vp==vn:
    print('Yes')
else:
    print('No')
