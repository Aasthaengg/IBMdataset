n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
b= [int(input()) for _ in range(m)]
c = []

for x in range(n):
    ci = 0
    for y in range(m):
        ci += A[x][y] * b[y]
    c.append(ci)

print(*[ci for ci in c], sep = "\n")