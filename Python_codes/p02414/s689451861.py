n,m,l = map(int,input().split())
A=[]
B=[]
for i in range(n):
    a = input().split()
    a_int= [int(s) for s in a ]
    A.append(a_int)
for j in range(m):
    b = input().split()
    b_int= [int(t) for t in b ]
    B.append(b_int)
i = 0
j = 0
Z = [[0 for q in range(l)] for p in range(n)]
for i in range(n):
    for t in range(l):
        z = 0
        for j in range(m):
            z += int(A[i][j])*int(B[j][t])
        Z[i][t]=z
i = 0
for i in range(n):
        print(' '.join(map(str,Z[i])))
