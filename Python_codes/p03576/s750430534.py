N,K = map(int,input().split())
XY = [list(map(int,input().split())) for i in range(N)]

ans = float("inf")
for i in range(N):
    x1,y1 = XY[i]
    for j in range(i+1,N):
        x2,y2 = XY[j]
        u2 = max(y1,y2)
        d2 = min(y1,y2)
        r2 = max(x1,x2)
        l2 = min(x1,x2)
        for k in range(j+1,N):
            x3,y3 = XY[k]
            u3 = max(u2,y3)
            d3 = min(d2,y3)
            r3 = max(r2,x3)
            l3 = min(l2,x3)
            for kk in range(k+1,N):
                x4,y4 = XY[kk]
                u4 = max(u3,y4)
                d4 = min(d3,y4)
                r4 = max(r3,x4)
                l4 = min(l3,x4)
                num = 0
                for m in range(N):
                    x,y = XY[m]
                    if l4<=x<=r4 and d4<=y<=u4:
                        num += 1
                if num >= K:
                    tmp = (u4-d4)*(r4-l4)
                    if tmp < ans:
                        ans = tmp
            num = 0
            for m in range(N):
                x,y = XY[m]
                if l3<=x<=r3 and d3<=y<=u3:
                    num += 1
            if num >= K:
                tmp = (u3-d3)*(r3-l3)
                if tmp < ans:
                    ans = tmp
        num = 0
        for m in range(N):
            x,y = XY[m]
            if l2<=x<=r2 and d2<=y<=u2:
                num += 1
        if num >= K:
            tmp = (u2-d2)*(r2-l2)
            if tmp < ans:
                ans = tmp
print(ans)