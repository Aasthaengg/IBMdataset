n, m, x = map(int,input().split())

c = []
a = []

for i in range(n):
    num = list(map(int,input().split()))
    c.append(num[0])
    a.append(num[1:])

cnt = 0

cost_t = n*10**5

for i in range(2**n):
    argo = [0 for _ in range(m)]
    cost = 0
    for j in range(n):
        if ((i >> j) & 1):
            cost += c[j]
            for k in range(m):
                argo[k] += a[j][k]

    if min(argo) >= x:
        cnt += 1
        if cost < cost_t:
            cost_t = cost
        
if cnt == 0:
    print(-1)
else:
    print(cost_t)