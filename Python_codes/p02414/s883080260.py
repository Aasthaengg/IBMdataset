n, m, l = map(int, input().split())

matrix_A = [list(map(int, input().split())) for _ in range(n)]
matrix_B = [list(map(int, input().split())) for _ in range(m)]

matrix_B_transposed  = list(map(list, zip(*matrix_B)))

for a in matrix_A:
    c = []
    for bt in matrix_B_transposed:
        c.append(sum(x * y for (x, y) in zip(a, bt)))
    print(*c)

