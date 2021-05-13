N=int(input())
*V,=map(int,input().split())

from collections import*
C1=Counter(V[::2])
C1=sorted(C1.items(),key=lambda x:x[1])
C2=Counter(V[1::2])
C2=sorted(C2.items(),key=lambda x:x[1])

K1=C1[-1][0]
V1=C1[-1][1]
K2=C2[-1][0]
V2=C2[-1][1]
if V1>V2:
    if K1==K2:
        V2=C2[-2][1]
elif V2>V1:
    if K1==K2:
        V1=C1[-2][1]
else:
    if K1==K2:
        if len(set(V))==1:
            V2=0
        else:
            V2=max(C1[-2][1],C2[-2][1])

print(N-V1-V2)