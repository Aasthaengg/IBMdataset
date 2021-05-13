h,w,d = map(int, input().split( ))
a = [list(map(int, input().split( ))) for i in range(h)]

p = [() for i in range(h*w)]

for i in range(h):
    for j in range(w):
        a[i][j] -= 1###
        p[a[i][j]] = (i,j)

def mp(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

p2 = [p[i::d] for i in range(d)]
p3 = [[mp(p2[j][i+1],p2[j][i]) for i in range(len(p2[j])-1)] for j in range(d)]
p4 = [[0] for j in range(d)]

for j in range(d):
    sm = 0
    for i in range(len(p3[j])):
        sm += p3[j][i]
        p4[j].append(sm)


q = int(input())

for i in range(q):
    li,ri = map(int,input().split( ))
    li-=1;ri-=1;##a[i]を取得したときに1引いているのでそろえる、これどちらかに統一したほうが
    j = li%d

    print(p4[j][ri//d]-p4[j][li//d])
