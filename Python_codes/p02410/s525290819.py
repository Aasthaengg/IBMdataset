n,m = map(int,raw_input().split())
mat = []
for k in range(n):
    mat.append(map(int,raw_input().split()))
b = []
for j in range(m):
    b.append(int(raw_input()))

for k in range(n):
    ans = 0
    for j in range(m):
        ans += mat[k][j]*b[j]
    print ans