H,W,M = map(int, input().split())
# grid = [[0 for _ in range(W)] for _ in range(H)]
bombs = set()

hc = [0 for h in range(H)]
wc = [0 for w in range(W)]

for _ in range(M):
    h,w = map(int, input().split())
    h-=1
    w-=1
    bombs.add((h, w))
    hc[h] += 1
    wc[w] += 1

hmax = max(hc)
wmax = max(wc)

htable = []
for h in range(H):
    if hc[h] == hmax:
        htable.append(h)

wtable = []
for w in range(W):
    if wc[w] == wmax:
        wtable.append(w)

# print(uw, uh)
#print(grid)
#print(wc, uw)
#print(hc, uh)

found = False
for h in htable:
    for w in wtable:
        if (h,w) not in bombs:
            print(hmax + wmax)
            exit(0)

print(hmax + wmax - 1)