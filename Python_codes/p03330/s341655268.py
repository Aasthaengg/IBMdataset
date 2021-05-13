N,C = map(int,input().split())
D = [list(map(int,input().split())) for i in range(C)]
c = [list(map(int,input().split())) for i in range(N)]
color = [{} for i in range(3)]
for h in range(N):
    for w in range(N):
        if c[h][w] not in color[(h+w+2)%3]:
            color[(h+w+2)%3][c[h][w]] = 1
        else:
            color[(h+w+2)%3][c[h][w]] += 1

ans = float('inf')
for c1 in range(1,C+1):
    for c2 in range(1,C+1):
        if c1 != c2:
            for c3 in range(1,C+1):
                if c1 != c3 and c2 != c3:
                    cand = 0
                    for k,v in color[0].items():
                        cand += D[k-1][c1-1]*v
                    for k,v in color[1].items():
                        cand += D[k-1][c2-1]*v
                    for k,v in color[2].items():
                        cand += D[k-1][c3-1]*v
                    ans = min(ans,cand)
print(ans)