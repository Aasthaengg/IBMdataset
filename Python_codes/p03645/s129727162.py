N,M = map(int,input().split())
ab_s = [list(map(int,input().split())) for _ in range(M)]
ONES = set()
NS = set()
for ab in ab_s:
    a = ab[0]
    b = ab[1]
    if a==1 or b==1:
        if a in NS or b in NS:
            print('POSSIBLE')
            break
        ONES.add(a)
        ONES.add(b)
    if a==N or b==N:
        if a in ONES or b in ONES:
            print('POSSIBLE')
            break
        NS.add(a)
        NS.add(b)
else:
    print('IMPOSSIBLE')
