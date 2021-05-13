n,m,c = map(int,input().split())
b = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]

cnt = 0

for i in range(n):
    value = c
    for j in range(m):
        value += a[i][j]*b[j]
    if value>0:
        cnt += 1

print(cnt)