h,w,d = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]

rui = [-1]*(h*w+1)
iti = [[] for _ in range(h*w+1)]

for i in range(h):
    for j in range(w):
        iti[a[i][j]] = (i,j)

for i in range(1,d+1):
    a = 0
    rui[i] = 0
    for j in range(i+d,h*w+1,d):
        a += (abs(iti[j][0] - iti[j-d][0]) + abs(iti[j][1] - iti[j-d][1]))
        rui[j] = a

q = int(input())
for _ in range(q):
    l,r = map(int,input().split())
    print(rui[r]-rui[l])