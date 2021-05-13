import copy
N=int(input())
T=list(map(int,input().split()))
M=int(input())
PX=[]
for i in range(M):
    PX.append(list(map(int,input().split())))
for i in range(M):
    A=copy.copy(T)
    A[PX[i][0]-1]=PX[i][1]
    print(sum(A))