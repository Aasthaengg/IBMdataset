
n,m = tuple([int(x) for x in raw_input().split(" ")])

A = []
for i in range(n):
    A.append([int(x) for x in raw_input().split(" ")])

v=[]
for i in range(m):
    v.append(int(raw_input()))

for i in range(n):
    s = 0
    for j in range(m):
        s += A[i][j]*v[j]
    print s