w,h,n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]
W = [0,w]
H = [0,h]
for x,y,a in xya:
    if a == 1:
        W[0] = max(W[0],x)
    elif a == 2:
        W[1] = min(W[1], x)
    elif a == 3:
        H[0] = max(H[0],y)
    else:
        H[1] = min(H[1], y)

print((W[1]-W[0])*(H[1]-H[0]) if W[0]<W[1] and H[0]<H[1] else 0)