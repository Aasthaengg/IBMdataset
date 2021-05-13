n,m = map(int,input().split())
a = [list(map(int,input().split(" "))) for i in range(n)]
f = [n] * m
for i in range(n):
    for j in range(a[i][0]):
        f[a[i][j+1]-1] -= 1
print(f.count(0))