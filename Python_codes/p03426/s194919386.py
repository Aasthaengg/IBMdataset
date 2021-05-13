h, w, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]

MAXH = 300
MAXW = 300

pos = [[] for _ in range(MAXH*MAXW+10)]
for i in range(h):
    for j in range(w):
        s = a[i][j]
        pos[s] = [i, j]

score = [0 for _ in range(MAXH*MAXW+10)]
for i in range(1, d+1):
    n = i
    while n+d <= h*w:
        x, y = pos[n]
        nx, ny = pos[n+d]
        score[n+d] += score[n]+abs(nx-x)+abs(ny-y)
        n += d

for loop in range(q):
    l, r = query[loop]
    print(score[r]-score[l])
