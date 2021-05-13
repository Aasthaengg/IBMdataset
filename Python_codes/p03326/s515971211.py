import numpy as np

N,M=list(map(int, input().split()))
A=[]
ret=[]
T=[[1,1,1],[1,1,-1],[1,-1,1],[-1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]]
for i in range(N):
    l=list(map(int, input().split()))
    l.append(0)
    A.append(l)

def Score(a):
    return abs(a[0])+abs(a[1])+abs(a[2])

for t in T:
    for a in A:
        a[3]=a[0]*t[0]+a[1]*t[1]+a[2]*t[2]
    A.sort(key=lambda x:x[3],reverse=True)
    score=0
    for _ in range(M):
        score+=A[_][3]
    ret.append(score)
ret.sort(reverse=True)
print(ret[0])