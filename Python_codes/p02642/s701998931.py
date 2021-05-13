import sys
N=int(sys.stdin.readline().strip())
A=map(int, sys.stdin.readline().split())
A.sort()
max_A=A[-1]

L=[ 0 for _ in range(max_A+1) ]
for a in A:
    L[a]+=1

for i,x in enumerate(L):
    if 1<x:
        L[i]=0

for a in A:
    for i in range(a*2,max_A+1,a):
        L[i]=0

print sum(L)