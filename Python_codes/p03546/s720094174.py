H,W=map(int,input().split())
c = []
for i in range(10):
    c.append(list(map(int,input().split())))

A = []
for i in range(H):
    A.append(list(map(int,input().split())))

c2 = [[0 for _ in range(10)]for _ in range(10)]

for i in range(10):
    for j in range(10):
        c2[i][j] = c[i][j]+c[j][1]

d = []
for i in range(10):
    d.append(min(c2[i]))

for _ in range(10):
    c2 = [[0 for _ in range(10)]for _ in range(10)]
    for i in range(10):
        for j in range(10):
            c2[i][j] = c[i][j]+d[j]
    d = []
    for i in range(10):
        d.append(min(c2[i]))
su = 0
for i in range(H):
    for j in range(W):
        if A[i][j] >=0:
            su+=d[A[i][j]]
print(su)
