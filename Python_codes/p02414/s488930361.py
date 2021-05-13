n,m,l = list(map(int,input().split()))
matrix_a = [list(map(int,input().split())) for i in range(n)]
matrix_b = [list(map(int,input().split())) for i in range(m)]
matrix_b = [list(x) for x in zip(*matrix_b)]

for i in range(n):
    line = []
    for j in range(l):
        line.append(sum([x*y for (x,y) in zip(matrix_a[i],matrix_b[j])]))
    print(' '.join(list(map(str,line))))