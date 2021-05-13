# 7_D
n,m,l=map(int,input().split())
A=[[0 for j in range(m)]for k in range(n)]
B=[[0 for j in range(l)]for k in range(m)]
C=[[0 for j in range(l)]for k in range(n)]
for j in range(n):
    var=list(map(int,input().split()))
    A[j]=var
for j in range(m):
    var=list(map(int,input().split()))
    B[j]=var

for j in range(n):
    for k in range(l):
        for t in range(m):
            C[j][k]+=A[j][t]*B[t][k]

for line in C:
    length=len(line)
    for col in line:
        length-=1
        if length ==0 :
            print(str(col))
        else:
            print(str(col)+" ",end='')
