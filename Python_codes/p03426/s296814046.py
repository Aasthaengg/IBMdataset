h,w,d = map(int,input().split())
lst = [0]*(h*w+1)
for i in range(h):
    a = list(map(int,input().split()))
    for j in range(w):
        lst[a[j]] = (i,j)
cost = [0]*(h*w+1)
for t in range(1,d+1):
    now = t
    while now <= h*w-d:
        nxt = now+d
        x0,y0 = lst[now]
        x1,y1 = lst[nxt]
        cost[nxt] = cost[now]+abs(x0-x1)+abs(y0-y1)
        now += d
q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(cost[r]-cost[l])