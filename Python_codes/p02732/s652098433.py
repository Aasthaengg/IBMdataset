N=int(input())
*A,=map(int,input().split())
from collections import*
C=Counter(A)
S=sum(v*(v-1)//2 for v in C.values())
for a in A:
    print(S-C[a]+1)