from collections import Counter

H,W=map(int,input().split())
a=[]
for i in range(H):
    a.extend(input())

v=list(Counter(a).values())
# print(v) #DB

f=True
if H%2==0 and W%2==0:    
    for e in v:
        if e%4!=0:
            f=False
            break
elif H%2==0 and W%2==1:
    q=0
    for e in v:
        if e%2!=0:
            f=False
            break
        elif e%4!=0:
            q+=1
            if q>H//2:
                f=False
                break
elif H%2==1 and W%2==0:
    q=0
    for e in v:
        if e%2!=0:
            f=False
            break
        elif e%4!=0:
            q+=1
            if q>W//2:
                f=False
                break
elif H%2==1 and W%2==1:
    p,q=0,0
    for e in v:
        if e%4==1:
            p+=1
            if p>1:
                f=False
                break
        elif e%4==3:
            f=False
            break
        elif e%4!=0:
            q+=1
            if q>(H-1)//2+(W-1)//2:
                f=False
                break
    if p==0:
        f=False

print('Yes' if f else 'No')