def getval():
    n,m = map(int,input().split())
    g = [[] for i in range(n)]
    for i in range(m):
        x,y = map(int,input().split())
        g[x-1].append(y-1)
    return n,m,g

def main(n,m,g):
    d = [-1 for i in range(n)]
    visited = [False for i in range(n)]
    temp = [[] for i in range(n)]
    ans = 0
    #print(g)
    #print(visited)
    for i in range(n):
        if d[i] != -1:
            continue
        q = [[i,-1]]
        prev = [-1]
        while q:
            idx = q.pop(-1)
            #print(i,idx,q,d)
            if not visited[idx[0]]:
                visited[idx[0]] = True
                if g[idx[0]]:
                    prev.append(idx[0])
                    for j in g[idx[0]]:
                        q.append([j,idx[0]])
                else:
                    d[idx[0]] = 0
                    temp[idx[1]].append(0)
                    if idx[1]==-1:
                        break
                    if prev[-1]!=-1 and q:
                        #print(q)
                        if q[-1][1]==idx[1]:
                            continue
                    bef = prev.pop(-1)
                    q.append([bef,prev[-1]])
            else:
                if d[idx[0]] == -1:
                    d[idx[0]] = 1 + max(temp[idx[0]])
                    if idx[1]!=-1:
                        temp[idx[1]].append(d[idx[0]])
                else:
                    if idx[1]!=-1:
                        temp[idx[1]].append(d[idx[0]])
                if prev[-1]!=-1 and q:
                    #print(q)
                    if q[-1][1]==idx[1]:
                        continue
                if idx[1]==-1:
                    break
                bef = prev.pop(-1)
                q.append([bef,prev[-1]])   
    print(max(max(d),0))
    #print(d)
                

if __name__=="__main__":
    n,m,g = getval()
    main(n,m,g)