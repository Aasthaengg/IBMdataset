n,m,l=map(int,input().split())
mat = [ list(map(int,input().split())) for _ in range(0,n) ]
mat2 = [ list(map(int,input().split())) for _ in range(0,m) ]
mat3 = [ [ 0 for _ in range(0,l) ] for _ in range(0,n) ]
for i in range(0,n):
    for j in range(0,m):
        for k in range(0,l):
            mat3[i][k] += mat[i][j] * mat2[j][k];
for xs in mat3:
    print(' '.join(map(str, xs)))