n , m , l = map( int,input().split())

A = [[0]*m]*n
B = [[0]*l]*m
#C = [[0]*l]*n エラーが起きてしまう
C = [[ 0 for x in range(l) ] for y in range(n)]

a = [[1, 2, 3], [4, 5, 6]]
a[1][1] = 7

for i in range(n):
    A[i] =  list( map( int,input().split()) )

for i in range(m):
    B[i] =  list( map( int,input().split()) )

for ni in range(n):
    
    for li in range(l):
        C_count = 0
        for mi in range(m):
            C_count += A[ni][mi] * B[mi][li]
        C[ni][li] = C_count

for a in C:
    print(*a, sep=' ')
