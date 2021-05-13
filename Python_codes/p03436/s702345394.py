from collections import defaultdict, deque
hwsss = [s.rstrip() for s in open(0)]
H,W = map(int, hwsss[0].split())
sss = [[int(c=='#') for c in list(l)] for l in hwsss[1:]]

dhw = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
]

# h,w,dist
dq = deque([(0, 0, 0)])
# h,w
queued = {(0, 0)}

fdist = -1
while dq:
    h, w, dist = dq.popleft()
    
    if h == H - 1 and w == W - 1:
        fdist = dist
        break
        
    for dh, dw in dhw:
        nh = h + dh
        nw = w + dw
        ndist = dist + 1

        if (nh,nw) in queued:
            continue
        if not(0 <= nh < H) or not(0 <= nw < W):
            continue
        if sss[nh][nw]:
            continue

        dq.append((nh, nw, ndist))
        queued.add((nh, nw))

if fdist == -1:
    print(-1)
else:
    print(H * W - sum(sum(sss,[])) - fdist - 1)