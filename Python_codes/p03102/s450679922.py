n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [(list(map(int,input().split()))) for i in range(n)]
t = 0

for i in range(n):
    z = 0
    for j in range(m):
        z += a[i][j] * b[j]
    z += c
    if z > 0:
        t += 1

print(t)    