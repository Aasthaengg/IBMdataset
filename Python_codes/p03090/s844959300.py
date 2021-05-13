n = int(input())
s = (n-1)*n//2

if n%2 == 1:

    g = [[] for _ in range(n)]
    for i in range(n):
        j = i+1
        if j != n:
            k = n-j
            #print(j, k)
            for a in range(1, n+1):
                if a == j or a == k:
                    continue
                else:
                    if a > j:
                        g[i].append(a-1)
        #else:
            #for a in range(1, n):
                #g[i].append(a-1)
    #print(g)
    cnt = 0
    edge = []
    for v in range(n):
        cnt += len(g[v])
        for u in g[v]:
            edge.append((v+1, u+1))
    print(cnt)
    for v, u in edge:
        print(v, u)

else:
    g = [[] for _ in range(n)]
    for i in range(n):
        j = i+1
        if j != n:
            k = n+1-j
            #print(j, k)
            for a in range(1, n+1):
                if a == j or a == k:
                    continue
                else:
                    if a > j:
                        g[i].append(a-1)
    cnt = 0
    edge = []
    for v in range(n):
        cnt += len(g[v])
        for u in g[v]:
            edge.append((v+1, u+1))
    print(cnt)
    for v, u in edge:
        print(v, u)
