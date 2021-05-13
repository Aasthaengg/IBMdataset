n, k = map(int, input().split())
xy = [list(map(int, input().split())) for i in range(n)]
xset = list(set([i[0] for i in xy]))
yset = list(set([i[1] for i in xy]))
xset.sort()
yset.sort()

W = len(xset)
H = len(yset)
ans = float('inf')
for ix in range(W):
    for jx in range(ix, W):
        for iy in range(H):
            for jy in range(iy, H):
                xmin = min(xset[ix], xset[jx])
                xmax = max(xset[ix], xset[jx])
                ymin = min(yset[iy], yset[jy])
                ymax = max(yset[iy], yset[jy])
                cnt = 0
                for x, y in xy:
                    if xmin<=x<=xmax and ymin<=y<=ymax:
                        cnt+=1
                if cnt>=k:
                    ans = min(ans, (xmax-xmin)*(ymax-ymin))
print(ans)
