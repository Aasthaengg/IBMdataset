import bisect

n,m = map(int,input().split())

dic = [[0] for i in range(n+1)]
city = []
for i in range(m):
    p,y = map(int,input().split())
    city.append((p,y))
    idx = bisect.bisect_left(dic[p],y)
    dic[p].insert(idx,y)

num = "000000"
for i in city:
    p,y = i[0],i[1]
    if len(str(p)) < 6:
        kami = num[:6-len(str(p))] + str(p)
    else:
        kami = str(p)
    simo = bisect.bisect_left(dic[p],y)
    if len(str(simo)) < 6:
        simo = num[:6-len(str(simo))] + str(simo)
    else:
        simo = str(simo)
    print(kami + simo)
