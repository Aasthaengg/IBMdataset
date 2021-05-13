import sys
sys.setrecursionlimit(10**6)
N = int(input())
A=list(map(int,input().split()))
Q = int(input())
BC = [map(int, input().split()) for _ in range(Q)]
B, C = [list(i) for i in zip(*BC)]
sum=0
D=[0]*(10**5+1)
for i in range(N):
    sum+=A[i]
    D[A[i]]+=1
for i in range(Q):
    D[C[i]]+=D[B[i]]
    sum+=D[B[i]]*(C[i]-B[i])
    D[B[i]]=0
    print(sum)
