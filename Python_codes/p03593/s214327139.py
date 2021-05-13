h,w=map(int,input().split())
from collections import Counter
c=Counter()
for i in range(h):
    s=list(input())
    c+=Counter(s)

if h==1 and w==1:
    print("Yes")
elif h==1:
    s2=w//2
    for k,v in c.items():
        c[k]-=2*(v//2)
        s2-=v//2
    if s2==0:
        print("Yes")
    else:
        print("No")
elif w==1:
    s2=h//2
    for k,v in c.items():
        c[k]-=2*(v//2)
        s2-=v//2
    if s2==0:
        print("Yes")
    else:
        print("No")
else:
    s4=((w//2)*(h//2))
    s2=0
    if w%2 and h%2:
        s2=(h+w-2)//2
    elif w%2:
        s2=(h//2)
    elif h%2:
        s2=w//2
    for k,v in c.items():
        s4-=v//4
        c[k]-=4*(v//4)
        s2-=c[k]//2
        c[k]-=2*(c[k]//2)
    if s4==0 and s2==0:
        print("Yes")
    else:
        print("No")
