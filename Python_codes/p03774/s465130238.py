from operator import itemgetter
n,m = map(int,input().split())
stu = list(list(map(int,input().split())) for i in range(n))
cp = list(list(map(int,input().split())) for i in range(m))

for sx,sy in stu:
    dis = {}
    cnt = 1
    for cx,cy in cp:
        dis[cnt] = (abs(sx - cx) + abs(sy - cy))
        cnt += 1
    print(min(dis.items(), key = itemgetter(1))[0])