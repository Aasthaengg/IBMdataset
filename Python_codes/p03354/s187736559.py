from collections import defaultdict
def main():
    n,m = map(int,input().split())
    p = list(map(int,input().split()))
    xy = sorted([tuple(map(int,input().split())) for _ in range(m)])
    d = defaultdict(list)
    for i in xy:
        d[i[0]].append(i[1])
        d[i[1]].append(i[0])
    searched = [False]*n
    c = 0
    graph = []
    allset = set(range(1,n+1))
    while allset:
        xxx = allset.pop()
        pool = set([xxx])
        searched[xxx-1] = True
        g = [xxx]
        gap = g.append
        pad = pool.add
        while pool:
            s = pool.pop()
            tmp = set(d[s])
            dif = tmp&allset
            dad = dif.add
            for i in dif:
                if searched[i-1] is False:
                    dad(i)
                    searched[i-1] = True
                    c += 1
                    gap(i)
                    allset.discard(i)
                    pad(i)
        graph.append(tuple(g))
    ans = 0
    for i in graph:
        ppp = set([p[j-1] for j in i])
        ans += len(ppp&set(i))
    print(ans)
    
if __name__ == '__main__':
    main()