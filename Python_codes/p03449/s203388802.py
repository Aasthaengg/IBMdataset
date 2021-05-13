N = int(input())
a = [list(map(int,input().split())) for i in range(2)]
b = []
for i in range(0,N):
    s = 0
    v = 0
    for j in range(0,i+1):
        s += a[0][j]
    for j in range(i,N):
        v += a[1][j]
    b.append(s+v)
print(max(b))