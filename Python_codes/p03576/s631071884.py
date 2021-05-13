N,K = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(N)]
xs = []
ys = []
for x,y in XY:
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()

def is_ok(l,r,d,u):
    k = 0
    for x,y in XY:
        if l <= x <= r and d <= y <= u:
            k += 1
            if k >= K:
                return True
    return False

ans = float('inf')
for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N-1):
            for l in range(k+1,N):
                l,r,d,u = xs[i],xs[j],ys[k],ys[l]
                if (r-l)*(u-d) >= ans: continue
                if is_ok(l,r,d,u):
                    ans = (r-l)*(u-d)
print(ans)