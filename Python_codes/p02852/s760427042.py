N,M=map(int,input().split())
S=input()[::-1]
L=[]
P=0

import sys
while P<N:
    k=0
    for i in range(1,M+1):
        if P+i>N:
            break
        if S[P+i]=='0':
            k=i
    if k==0:
        print(-1)
        sys.exit()
    L.append(k)
    P+=k

L=L[::-1]
print(*L)