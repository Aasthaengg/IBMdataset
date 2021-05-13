n, m = map(int, input().split())
edges = [[] for i in range(n)]
for i in range(m):
    li, ri, di = map(int, input().split())
    li, ri = li-1, ri-1
    edges[li].append((ri, di))
    edges[ri].append((li, -di))

coordinate = [None for i in range(n)]
for i in range(n):
    if coordinate[i] == None:
        coordinate[i] = 0
    else:
        continue
    nodes = [i]
    while nodes != []:
        next_nodes = []
        for node in nodes:
            edge = edges[node]
            start = coordinate[node]
            for end, dist in edge:
                if coordinate[end] == None:
                    coordinate[end] = start + dist
                    next_nodes.append(end)
                else:
                    if coordinate[end] != start + dist:
                        print('No')
                        exit()
        nodes = next_nodes[:]
print('Yes')