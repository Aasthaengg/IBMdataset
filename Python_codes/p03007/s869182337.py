# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

N=int(input())
A=list(map(int,input().split()))
A.sort()
B=[x for x in A if x>=0]
C=[x for x in A if x<0]
ans=[]
if B and C:
    P=B.pop()
    M=C.pop()
    for x in B:
        ans.append((M,x))
        M-=x
    for x in C:
        ans.append((P,x))
        P-=x
    ans.append((P,M))
    P-=M
    print(P)
    for row in ans:
        print(*row)
elif B:
    M=B[0]
    P=B.pop()
    for x in B[1:]:
        ans.append((M,x))
        M-=x
    ans.append((P,M))
    P-=M
    print(P)
    for row in ans:
        print(*row)
else:
    P=C.pop()
    for x in C:
        ans.append((P,x))
        P-=x
    print(P)
    for row in ans:
        print(*row)