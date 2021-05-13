h,w=map(int,input().split())
a=[]
import collections
c=collections.Counter() 
for i in range(h):
    s=input()
    a.append(s)
    for j in s:
        c[j]+=1
l=c.most_common()
if h%2==1:
    n=h-1
else:
    n=h
if w%2==1:
    m=w-1
else:
    m=w
p=n*m
r=(h*w-p)%2
q=(h*w-p)-r

for i,j in l:
    if j>=4 and p>=4:
        tmp=min(j-j%4,p)
        p-=tmp
        j-=tmp
    if j>=2 and q>=2:
        tmp=min(j-j%2,q)
        q-=tmp
        j-=tmp
    if j>=1 and r==1:
        r=0
        j=0
    elif j==1 and r==0:
        print("No")
        exit()
if p+q+r==0:
    print("Yes")
else:
    print("No") 






