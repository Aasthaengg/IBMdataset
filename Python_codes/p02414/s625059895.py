n,m,l=[int(x) for x in input().split()]
A=[[0 for _ in range(m)] for _ in range(n)]
B=[[0 for _ in range(l)] for _ in range(m)]
C=[[0 for _ in range(l)] for _ in range(n)]
for i in range(n):
    A[i]=[int(x) for x in input().split()]
for i in range(m):
    B[i]=[int(x) for x in input().split()]
B_transpose=list(map(list,zip(*B)))
for i in range(n):
    for j in range(l):
        C[i][j]=sum([x*y for x,y in zip(A[i],B_transpose[j])])
    print(" ".join([str(x) for x in C[i]]))