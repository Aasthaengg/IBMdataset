N,K = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(N)]
xs = []
ys = []
for x,y in XY:
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()

ans = float('inf')
for l in range(N-1):
    for r in range(l+1,N):
        w = xs[r] - xs[l]
        for d in range(N-1):
            for u in range(d+1,N):
                h = ys[u] - ys[d]
                if ans <= w*h: continue
                c = 0
                for x,y in XY:
                    if xs[l] <= x <= xs[r] and ys[d] <= y <= ys[u]:
                        c += 1
                        if c >= K:
                            ans = w*h
                            break
print(ans)