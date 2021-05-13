M, K = map(int, input().split())
if K >= 2**M:
    print(-1)
elif M == 0:
    print(0, 0)
elif M == 1:
    if K == 0:
        print("0 0 1 1")
    else:
        print(-1)
elif K==0:
    r = list(range(2**M))
    r += r[::-1]
    print(*r)
else:
    d = set()
    for i in range(2**M):
        p = tuple(sorted([i, i^K]))
        if p not in d:
            d.add(p)
    r = []
    while d:
        x,y = d.pop()
        z,w = d.pop()
        r += [x,y,z,w,y,x,w,z]
    print(*r)

