from collections import defaultdict

def find(tab, a):
    if tab[a] == -1: return a
    tab[a] = find(tab, tab[a])
    return tab[a]

def union(tab, a, b):
    pa, pb = (find(tab, a), find(tab, b))
    if pa!=pb:
        tab[pb] = pa

H,W=map(int,input().split())
S=[input() for _ in range(H)]
N=H*W
tab = [-1]*N

for y in range(H):
    for x in range(W):
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            xx=x+dx
            yy=y+dy
            if xx < 0 or xx>=W or yy<0 or yy>=H:
                continue
            src = W*y+x
            dst = W*yy+xx
            if S[y][x]!=S[yy][xx]:
                union(tab, src, dst)
dic = defaultdict(lambda: {"#":0,".":0})
for i in range(N):
    p = find(tab, i)
    t = S[i//W][i%W]
    dic[p][t]+=1

ans = 0
for d in dic.values():
    ans += (d["#"]*d["."])
print(ans)
