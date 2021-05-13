import sys
sys.setrecursionlimit(10000000)
N, Q = map(int, input().split())

ARR = []

for i in range(N-1):
    ARR.append(list(map(int, input().split())))

BRR = []

for i in range(Q):
    BRR.append(list(map(int, input().split())))


def prepare(n, q, arr, brr):
    nodePoints = [0 for i in range(n)]
    for i in range(q):
        nodeIndex = brr[i][0] - 1
        nodePoints[nodeIndex] += brr[i][1]

    nodes = [[] for i in range(n)]

    for i in range(n - 1):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1

        nodes[startNode].append(endNode)
        nodes[endNode].append(startNode)

    return nodes, nodePoints


nodes, nodePoints = prepare(N, Q, ARR, BRR)


def dfs(currentNode, nodes, parentNode=-1, parentPoint=0):
    nodePoints[currentNode] = nodePoints[currentNode] + parentPoint
    childNodes = nodes[currentNode]
    for childNode in childNodes:
        if childNode == parentNode:
            continue
        dfs(childNode, nodes, currentNode, nodePoints[currentNode])


dfs(0, nodes)

print(" ".join([str(nodePoints[i]) for i in range(N)]))
