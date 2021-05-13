from itertools import accumulate
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
AS=sum(A)
BS=sum(B)
if BS>AS:
    print(-1)
elif all(a>=b for a,b in zip(A,B)):
    print(0)
else:
    cap=sum(max(0,b-a) for a,b in zip(A,B))
    M=sum(b-a>0 for a,b in zip(A,B))
    C=sorted((a-b for a,b in zip(A,B)),reverse=True)
    D=list(accumulate(C))
    for i, d in enumerate(D,1):
        if cap<=d:
            print(i+M)
            break