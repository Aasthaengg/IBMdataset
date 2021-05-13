import copy
h,w = map(int,input().split())
g = [[False]*(w+2) for _ in range(h+2)]
d = [[-1]*(w+2) for _ in range(h+2)]
ans = 0
for i in range(h):
    l = list(input())
    for j in range(w):
        if l[j] == ".":
            ans += 1
            g[i+1][j+1] = True
def f(i,j):
    return [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
now = f(1,1)
d[1][1] = 0
nxt = []
cnt = 1
while now:
    for l in now:
        i,j = l[0],l[1]
        if d[i][j] == -1 and g[i][j]:
            d[i][j] = cnt
            for l2 in f(i,j):
                nxt.append(l2)
    cnt += 1
    now = copy.copy(nxt)
    nxt = []
if d[h][w] == -1:
    print(-1)
else:
    print(ans-d[h][w]-1)