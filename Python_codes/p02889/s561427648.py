def solve():
    INF = float('inf')

    def Dijkstra(adjList, vSt):
        numV = len(adjList)
        useds = [False] * numV
        fuels = [-1] * numV
        fuels[vSt] = L
        nums = [INF] * numV
        num = 0
        vs = set([vSt])
        while vs:
            vNexts = set()
            fuelNexts = [-1] * numV
            while vs:
                fNow, vNow = -1, -1
                for v in vs:
                    if fuels[v] > fNow:
                        fNow, vNow = fuels[v], v
                nums[vNow] = num
                useds[vNow] = True
                vs.remove(vNow)

                fuel = fuels[vNow]
                for v2, wt in adjList[vNow]:
                    if useds[v2]: continue
                    if fuel >= wt:
                        if fuel-wt > fuels[v2]:
                            fuels[v2] = fuel-wt
                        vs.add(v2)
                    elif L >= wt:
                        if L-wt > fuelNexts[v2]:
                            fuelNexts[v2] = L-wt
                        vNexts.add(v2)

            vs = set([v for v in vNexts if not useds[v]])
            fuels = fuelNexts
            num += 1
        return nums


    N, M, L = map(int, input().split())
    adjL = [[] for _ in range(N)]
    for _ in range(M):
        A, B, C = map(int, input().split())
        A, B = A-1, B-1
        adjL[A].append((B, C))
        adjL[B].append((A, C))

    numss = []
    for v in range(N):
        nums = Dijkstra(adjL, v)
        numss.append(nums)

    Q = int(input())
    anss = []
    for _ in range(Q):
        s, t = map(int, input().split())
        s, t = s-1, t-1
        if numss[s][t] == INF:
            anss.append(-1)
        else:
            anss.append(numss[s][t])

    print('\n'.join(map(str, anss)))


solve()
