H,W=map(int,input().split())
D={}
for y in range(H):
    S=input()
    for s in S:
        if s in D:
            D[s]+=1
        else:
            D[s]=1

if (H%2)+(W%2)==0:
    F=True
    for s in D:
        if D[s]%4:
            F=False
elif (H%2)+(W%2)==1:
    if H%2:
        H,W=W,H

    F=True
    G=0
    for s in D:
        if D[s]%2:
            F=False
        elif D[s]%4==2:
            G+=1
    if G>H//2:
        F=False
else:
    G=0
    I=0
    for s in D:
        if D[s]%2:
            I+=1
        elif D[s]%4==2:
            G+=1
    F=(I==1) and (G<=(H+W-2)//2)

if F:
    print("Yes")
else:
    print("No")
