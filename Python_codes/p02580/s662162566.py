import heapq
H, W, M = map(int, input().split())
bomb = []
for i in range(M):
    h, w = map(int, input().split())
    h-=1; w-=1
    bomb.append((h, w))

row = [0] * H
col = [0] * W

for h, w in bomb:
    row[h] += 1
    col[w] += 1

lmax = max(row) + max(col)
row = [(r, i) for i, r in enumerate(row)]
col = [(c, i) for i, c in enumerate(col)]
row.sort(reverse=True)
col.sort(reverse=True)
bomb = set(bomb)

for r, i in row:
    for c, j in col:
        if r+c < lmax: break
        if not (i, j) in bomb:
            print(lmax)
            exit()
print(lmax-1)
