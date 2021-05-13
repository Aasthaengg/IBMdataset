import queue 
MOD = 10**9 +7
INF = 10**9
def main():
    n,m = map(int,input().split())
    V0 = [[] for _ in range(n)]
    V1 = [[] for _ in range(n)]
    V2 = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        V0[u].append(v)
        V1[u].append(v)
        V2[u].append(v)
    
    s,t = map(int,input().split())
    s -= 1
    t -= 1
    
    d0 = [-1]*n
    d1 = [-1]*n
    d2 = [-1]*n
    d0[s] = 0

    q = queue.Queue()
    q.put([s,0])
    while q.qsize() != 0:
        p = q.get()
        mod = p[1]
        v = p[0]
        if mod == 0:
            for e in V0[v]:
                if d1[e] == -1:
                    d1[e] = d0[v] + 1
                    q.put([e,1])

        elif mod == 1:
            for e in V1[v]:
                if d2[e] == -1:
                    d2[e] = d1[v] + 1
                    q.put([e,2])
        
        else:
            for e in V2[v]:
                if d0[e] == -1:
                    d0[e] = d2[v] + 1
                    q.put([e,0])
    
    if d0[t] == -1:
        print(-1)
    else:
        print(d0[t]//3)
   
if __name__=='__main__':
    main()

