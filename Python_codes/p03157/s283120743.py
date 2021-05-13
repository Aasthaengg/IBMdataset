from collections import deque
h , w = map(int,input().split())
ma = [list(input()) for i in range(h)]
visit = [[False for i in range(w)] for j in range(h)]
ans = 0
muki = [(0,1),(0,-1),(1,0),(-1,0)]
for i in range(h):
    for j in range(w):
        if ma[i][j] == "#" and not visit[i][j]:
            visit[i][j] = True
            d = deque()
            d.append((i,j,1))
            kuro = 1
            siro = 0
            while d:
                nowx , nowy , p = d.popleft()
                for a,b in muki:
                    nex = nowx + a
                    ney = nowy + b
                    if 0 <= nex <= h-1 and 0 <= ney <= w-1:
                        if not visit[nex][ney]:
                            if p == 1 and ma[nex][ney] == ".":
                                d.append((nex,ney,0))
                                siro += 1
                                visit[nex][ney] = True
                            if p == 0 and ma[nex][ney] == "#":
                                d.append((nex,ney,1))
                                kuro += 1
                                visit[nex][ney] = True
            ans += kuro*siro
print(ans)