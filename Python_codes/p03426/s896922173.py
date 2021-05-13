

def cost(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def submit():
    h, w, d = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    
    pos = {}
    for i in range(h):
        for j in range(w):
            pos[a[i][j]] = (i, j)

    dist = {}
    for i in range(1, d + 1):
        dist[i] = {i: 0}
        nxt = i + d
        while nxt <= h * w:
            dist[i][nxt] = dist[i][nxt - d] + cost(pos[nxt - d], pos[nxt])
            nxt += d
    
    q = int(input())
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        base = l % d
        if base == 0:
            base = d
        ans.append(dist[base][r] - dist[base][l])
        
    for a in ans:
        print(a)


submit()
            
    
