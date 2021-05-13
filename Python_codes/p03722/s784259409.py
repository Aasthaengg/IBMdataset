def main():
    import sys
    #input = sys.stdin.readline
    
    N,M = map(int, input().split())
    G = [[] for i in range(N+2)]
    iG = [[] for i in range(N+2)]
    E = []
    for i in range(M):
        a,b,c = map(int,input().split())
        G[a].append([b,-c])
        iG[b].append([a,-c])
        E.append([a,b,c])
        
    from1 = [0]*(N+2)
    toN = [0]*(N+2)
    que = [1]
    while que != []:
        v = que.pop()
        from1[v] = 1
        for L in G[v]:
            b,c = L
            if from1[b] == 0:
                que.append(b)
    que = [N]
    while que != []:
        v = que.pop()
        toN[v] = 1
        for L in iG[v]:
            b,c = L
            if toN[b] == 0:
                que.append(b)
    
    oneN = [0]*(N+2)
    for i in range(N+1):
        oneN[i] = from1[i]*toN[i]
    
    
    itG =[[] for i in range(N+2)]
    for e in E:
        a,b,c = e
        if oneN[a]==oneN[b]==1:
            itG[b].append([a,-c])
            
    import copy
    cost = [float("inf")]*(N+2)
    cost[1] = 0
    for i in range(N+2):
        tmpcost = copy.deepcopy(cost)
        for j in range(1,N+1):
            for e in itG[j]:
                a,c = e
                #print(j,a,c)
                tmpcost[j] = min(tmpcost[j], cost[a]+c)
                #print(tmpcost)
        #print(tmpcost)
        cost = copy.deepcopy(tmpcost)
    flag = 0
    tmpcost = copy.deepcopy(cost)
    for j in range(1,N+1):
        for e in itG[j]:
            a,c = e
            if cost[a]+c < cost[j]:
                #print(cost[a]+c)
                flag = 1
                break
    #print(from1)
    #print(toN)
    #print(oneN)
    #print(itG)
    #print(tmpcost)
    if flag == 1:
        print("inf")
    else:
        print(-cost[N])
    
    
    
main()