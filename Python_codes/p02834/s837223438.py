def main():
    from collections import defaultdict,deque
    from math import ceil
    from sys import setrecursionlimit
    setrecursionlimit(10**6)
    f = lambda :map(int,input().split())
    n,u,v = f() # u:高橋
    edge = defaultdict(list)
    for i in range(n-1):
        a,b = f()
        edge[a].append(b)
        edge[b].append(a)
    
    distance = [[-1]*2 for _ in range(n+1)]
    distance[u][0] = 0
    distance[v][1] = 0
    def dfs(node,start):
        targets = deque([node])
        while targets:
            parent = targets.popleft()
            distance_parent = distance[parent][start]
            for child in edge[parent]:
                if distance[child][start] == -1:
                    distance[child][start] = distance_parent + 1
                    targets.append(child)
    dfs(u,0)
    dfs(v,1)
    ans = 0
    for u_d, v_d in distance:
        if u_d < v_d:
            ans = max(ans,v_d)
    print(ans-1)


        


main()
        



                
        
        
        
        
        



    
