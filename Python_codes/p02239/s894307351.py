def main():
    import sys
    N = int(sys.stdin.readline())
    L1 = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    L = [[] for _ in range(N+1)]
    for row in L1:
        L[row[0]] += row[2:]
    #print(L)
    
    d = [-1 for i in range(N+1)] #距離
    def bfs(p, queue=[]):
        queue+=[p]
        d[p]=0
        while queue:
            now = queue.pop(0)
            for ch in L[now]:
                if d[ch] ==-1: #未開
                    d[ch] = d[now]+1
                    queue +=[ch]
    
    
    bfs(1)
    for idx, ans in enumerate(d[1:]):
        print(idx+1, ans)


if __name__=='__main__':
    main()
