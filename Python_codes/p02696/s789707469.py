import math
A,B,N=map(int,input().split())
han=0
kot=0
i=0
if B==1:
    print(0)
    exit()
if B-1>=N:
    print(math.floor(A*N/B)-A*math.floor(N/B))
    i=1
else:
    for a in range(B-1,N,B):
        if han<(math.floor(A*a/B)-A*math.floor(a/B)):
            han=(math.floor(A*a/B)-A*math.floor(a/B))
            kot=a

if i==0:
    print(han)