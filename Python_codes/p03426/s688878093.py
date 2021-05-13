h,w,D = map(int,input().split())
a = [[int(i) for i in input().split()] for _ in range(h)]
px = [0]*(h*w+1)
py = [0]*(h*w+1)
d = [0]*(h*w+1)

for i in range(h):
    for j in range(w):
        px[a[i][j]] = i
        py[a[i][j]] = j

for i in range(D+1,h*w+1):
    d[i] = d[i-D] + abs(px[i]-px[i-D]) + abs(py[i]-py[i-D])

q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    print(d[r]-d[l])