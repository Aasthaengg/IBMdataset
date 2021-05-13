w,h,n = map(int,input().split())
l = [[0] * w for i in range(h)]
z = [list(map(int,input().split())) for i in range(n)]
x,y,a = [list(i) for i in zip(*z)]

for i in range(n):
    if a[i] == 1:
        for j in range(h):
            for k in range(x[i]):
                l[j][k] = 1
    if a[i] == 2:
        for j in range(h):
            for k in range(x[i],w):
                l[j][k] = 1
    if a[i] == 3:
        for j in range(y[i]):
            for k in range(w):
                l[j][k] = 1
    if a[i] == 4:
        for j in range(y[i],h):
            for k in range(w):
                l[j][k] = 1

t = 0
for i in range(h):
    t += l[i].count(0)

print(t)