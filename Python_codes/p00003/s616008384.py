n = int(raw_input())
for i in range(n):
    edge = map(int,raw_input().split(" "))
    e0 = edge[0] * edge[0]
    e1 = edge[1] * edge[1]
    e2 = edge[2] * edge[2]
    ret = "NO"
    if (edge[0] > edge[1]) and (edge[0] > edge[2]):
        if (e0 - e1 - e2) == 0:
            ret = "YES"
    if (edge[1] > edge[0]) and (edge[1] > edge[2]):
        if (e1 - e0 - e2) == 0:
            ret = "YES"
    if (edge[2] > edge[0]) and (edge[2] > edge[1]):
        if (e2 - e0 - e1) == 0:
            ret = "YES"
    print ret