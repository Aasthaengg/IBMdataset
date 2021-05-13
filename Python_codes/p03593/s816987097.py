h,w=map(int,input().split())
a=[input() for _ in range(h)]
from collections import defaultdict
d=defaultdict(lambda:0)
for ai in a:
    for aij in ai:
        d[aij]+=1
if h%2==0 and w%2==0:
    print('Yes' if all(v%4==0 for v in d.values()) else 'No')
elif h%2==0 and w%2==1:
    c=0
    for v in d.values():
        if v%4==0:
            pass
        elif v%2==0:
            c+=1
        else:
            print('No')
            exit()
    print('Yes' if c<=h//2 else 'No')
elif h%2==1 and w%2==0:
    c=0
    for v in d.values():
        if v%4==0:
            pass
        elif v%2==0:
            c+=1
        else:
            print('No')
            exit()
    print('Yes' if c<=w//2 else 'No')
else:
    ce=0
    co=0
    for v in d.values():
        if v%4==0:
            pass
        elif v%2==0:
            ce+=1
        else:
            co+=1
    print('Yes' if ce<=h//2+w//2 and co==1 else 'No')
