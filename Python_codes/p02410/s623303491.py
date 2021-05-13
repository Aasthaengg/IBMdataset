n, m = map(int, input().split())
a = [[int(num) for num in input().split()] for i in range(n)]
b = [int(input()) for i in range(m)]
for i in range(n):
    c = 0
    for j in range(m):
        c += a[i][j] * b[j]
    print(c)