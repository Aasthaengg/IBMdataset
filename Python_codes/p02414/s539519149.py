#coding:utf-8
#1_7_D 2015.4.7
n,m,l = map(int,input().split())
matrixA = [list(map(int,input().split())) for i in range(n)]
matrixB = [list(map(int,input().split())) for i in range(m)]

matrixAxB = [list(sum([matrixA[i][k] * matrixB[k][j] for k in range(m)]) for j in range(l)) for i in range(n)]

for row in matrixAxB:
    print(*row)