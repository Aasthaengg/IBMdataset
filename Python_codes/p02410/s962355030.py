n, m = list(map(int, input().split()))
matrix_a = [list(map(int, input().split())) for i in range(n)]
matrix_b = [int(input()) for i in range(m)]
for i in range(n):
    print(sum([x*y for (x,y) in zip(matrix_b,matrix_a[i])]))