h,w=map(int,input().split())
from collections import Counter
l=[]
for _ in range(h):
    l+=list(input())
c=Counter(l)

if h==1 and w==1:
    print("Yes")
elif h==1:
    two=w//2
    for k,v in c.items():
        c[k]-=2*(v//2)
        two-=v//2
    if two==0:
        print("Yes")
    else:
        print("No")
elif w==1:
    two=h//2
    for k,v in c.items():
        c[k]-=2*(v//2)
        two-=v//2
    if two==0:
        print("Yes")
    else:
        print("No")
else:
    four=((w//2)*(h//2))
    two=0
    if w%2==1 and h%2==1:
        two=(h+w-2)//2
    elif w%2==1:
        two=h//2
    elif h%2==1:
        two=w//2
    for k,v in c.items():
        four-=v//4
        c[k]-=4*(v//4)
        two-=c[k]//2
        c[k]-=2*(c[k]//2)

    if four==0 and two==0:
        print("Yes")
    else:
        print("No")
