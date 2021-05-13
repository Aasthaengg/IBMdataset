n,m = map(int,input().split())
ab = [0]*n
cd = [0]*m
for i in range(n):
    ab[i] = list(map(int,input().split()))
for i in range(m):
    cd[i] = list(map(int,input().split())) + [i]
for a,b in ab:
    dis = [0]*m
    for c,d,i in cd:
        dis[i] = [abs(a-c) + abs(b-d)] + [i+1]
    dis.sort(key= lambda val : val[0])
    print(dis[0][1])
