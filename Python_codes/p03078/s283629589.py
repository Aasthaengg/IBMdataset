import heapq
x,y,z,k = map(int,input().split())
a = sorted(list(map(int,input().split())),reverse = 1)
b = sorted(list(map(int,input().split())),reverse = 1)
c = sorted(list(map(int,input().split())),reverse = 1)
q = []
heapq.heapify(q)
for i in range(x):
    if i == 0:
        jlim = y
    else:
        jlim = min(-(-k//i),y)
    for j in range(jlim):
        if i*j == 0:
            llim = z
        else:
            llim = min(-(-k//(i*j)),z)
        for l in range(llim):
            heapq.heappush(q,-(a[i]+b[j]+c[l]))
for i in range(k):
    x = heapq.heappop(q)
    print(-x)

