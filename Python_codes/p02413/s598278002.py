r, c = list(map(int, input().split(" ")))
A = [[0 for _ in range(c)] for _ in range(r)]

A_sum = 0
for i in range(r):
    a_line = list(map(int, input().split(" ")))
    for j, a in enumerate(a_line):
        print("%d "%a, end="")
        A[i][j] = a
        A_sum += a
    print("%d"%sum(a_line))

A_T = list(map(list, zip(*A)))
for a_t in A_T:
    print ("%d "%(sum(a_t)), end="")

print (A_sum)