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
    #Loop through each vertex
    for i in range(n):
        #If already computed: pass
        if d[i] != -1:
            continue
        q = [[i,-1]]
        prev = [-1]
        while q:
            idx = q.pop(-1)
            cur = idx[0]
            #If not visited
            if not visited[cur]:
                visited[cur] = True
                #If there are vertices that can be reached
                if g[cur]:
                    prev.append(cur)
                    #Append to q
                    for j in g[cur]:
                        q.append([j,cur])
                    continue
                #No vertices to be reached
                else:
                    d[cur] = 0
                    temp[idx[1]].append(0)
            #If it has been visited in some way
            else:
                #If the distance hasn't been computed
                if d[cur] == -1:
                    d[cur] =  1 + max(temp[cur])
                if idx[1] != -1:
                    temp[idx[1]].append(d[cur])
            #If this is the first vertex
            if prev[-1] == -1:
                break
            #If the next vertex has the same parent vertex
            if q:
                if q[-1][1]==idx[1]:
                    continue
            #Otherwise, return to the parent node
            par = prev.pop(-1)
            q.append([par,prev[-1]])

    print(max(max(d),0))

if __name__=="__main__":
    n,m,g = getval()
    main(n,m,g)