from collections import Counter
n=int(input())
a=list(map(int, input().split()))

c=Counter(a)
bl=True
if n%3==0:
    if len(c.keys())==3:
        l=[]
        for i,j in c.items():
            if j!=n//3:
                bl=False
            l.append(i)
        if 0 in l:
            bl=False
        if l[0]^l[1]!=l[2]:
            bl=False
    elif len(c.keys())==2:
        if c[0]!=n//3:
            bl=False
    else:
        bl=False
else:
    bl=False
if c[0]==n:
    bl=True

if bl:
    print("Yes")
else:
    print("No")