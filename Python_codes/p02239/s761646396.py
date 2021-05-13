n = int(input())

m = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    tmp = [int(x) for x in input().split()]
    u = tmp[0]
    k = tmp[1]
    l = tmp[2:]
    for x in l:
        m[u-1][x-1] = 1

dl = [float('inf') for _  in range(n)]
dl[0] = 0

q = [0]

while q:
    t = q.pop()
    tl = m[t]
    for i,x in enumerate(tl):
        if x == 1:
            if dl[i] > dl[t] + 1:
                q.append(i)
                dl[i] = dl[t] + 1
            else:
                pass
        else:
            pass


for i,x in enumerate(dl):
    if x == float('inf'):
        print(i+1, -1)
    else:
        print(i+1, x)

