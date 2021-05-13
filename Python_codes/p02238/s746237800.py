def main():
    import sys
    N = int(sys.stdin.readline())
    L1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    #print(L1)
    edge = [[] for _ in range(N+1)]
    for row in L1:
        for ele in row[2:]:
            edge[row[0]].append(ele)
            #edge[ele].append(row[0])

    #print(edge)
    sys.setrecursionlimit(1000)
    
    go = [-1 for _ in range(N+1)]
    go[0], go[1] =0, 1
    back = [-1 for _ in range(N+1)]
    
    d = [1]
    def dfs(p):
        if edge[p]:
            for c in edge[p]:
                if go[c]==-1:
                    d[0]+=1
                    go[c] = d[0]
                    dfs(c)
        
        #抜ける順
        d[0]+=1
        back[p] =d[0]
                
    dfs(1)
    for i in range(2, N+1):
        if go[i] ==-1:
            d[0]+=1
            go[i] = d[0]
            dfs(i)
    for i in range(1, N+1):
        print(i, go[i], back[i])




if __name__=='__main__':
    main()
