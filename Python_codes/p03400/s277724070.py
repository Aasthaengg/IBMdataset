N=int(input())
D,X=map(int,input().split())
A=[]
for i in range(N):
    A.append(int(input()))
D=D-1
for i in range(N):
    X=X+(D//A[i])
print(X+N)