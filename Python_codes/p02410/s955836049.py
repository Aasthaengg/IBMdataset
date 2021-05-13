n,m = map(int,input().split())

matrix_a = [list(map(int,input().split(" "))) for i in range(n)]

matrix_b = [int(input()) for i in range(m)]

for i in range(n):
    answer = sum([matrix_a[i][j] * matrix_b[j] for j in range(m)])
    print(answer)