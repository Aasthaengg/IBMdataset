h, w = map(int, input().split())
g = []
for i in range(h):
    g += list(map(int, input().split()))
res = []
for j in range(h):
    for i in range(w):
        for k in [(1,0),(0,1)]:
            if i+k[0]>=0 and i+k[0]<w and j+k[1]>=0 and j+k[1]<h:
                idx_cur = j * w + i
                idx_nex = (j+k[1]) * w + i+k[0]
                if g[idx_cur] % 2 != 0:
                    g[idx_cur] -= 1
                    g[idx_nex] += 1
                    res.append([j+1,i+1,j+k[1]+1,i+k[0]+1])
print(len(res))
for i in res:
    print(*i)