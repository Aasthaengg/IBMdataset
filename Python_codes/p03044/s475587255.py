import collections
def resolve():
    N = int(input())
    VVW = [list(map(int, input().split())) for _ in range(N-1)]
    adjs = [[] for _ in range(N)]
    for vvw in VVW:
        adjs[vvw[0]-1].append([vvw[1]-1, vvw[2]])
        adjs[vvw[1]-1].append([vvw[0]-1, vvw[2]])

    result = [None for _ in range(N)]
    deq = collections.deque([[0, 0]])
    result[0] = "0"

    while deq:
        node, cost = deq.popleft()
        for adj in adjs[node]:
            nextnode, nextcost = adj[0], adj[1]
            if result[nextnode] is not None:
                continue
            if nextcost%2 == 0:
                result[nextnode] = result[node]
            else:
                result[nextnode] = "1" if result[node] == "0" else "0"
            deq.append([nextnode, nextcost])
    
    [print(r) for r in result]



if '__main__' == __name__:
    resolve()