n,m = map(int, input().split())
link = []
for i in range(m):
    tmp = list(map(int,input().split()))
    link.append([tmp[0]-1,tmp[1]-1,-tmp[2]])

def bell(edges, start,num_v):
    cost = [float('inf')] * num_v
    cost[start] = 0
    for _ in range(num_v):
        updated = False
        for a, b, c in edges:
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated: break
    else:
        return -1,cost
    return 1,cost

ans1,d = bell(link,0,n)

if ans1 == -1:
    inf_flag = [False]*n
    for i in range(n):
        for f, t, c in link:
            if d[f] == float("inf"): continue
            if inf_flag[f] == True:
                inf_flag[t] = True
            if d[t] > d[f] + c:
                d[t] = d[f] + c
                inf_flag[t] = True
    print("inf" if inf_flag[n-1] else -d[n-1])
else:
    print(-d[-1])