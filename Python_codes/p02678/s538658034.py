from collections import deque

N, M = map(int, input().split())
ARR = []

for i in range(M):
    ARR.append(list(map(int, input().split())))


def prepare(n, m, arr):
    nodes = [[] for i in range(n)]
    nodeStatus = [False for i in range(n)]
    for i in range(m):
        startNode = arr[i][0] - 1
        endNode = arr[i][1] - 1

        nodes[startNode].append(endNode)
        nodes[endNode].append(startNode)

    return nodes, nodeStatus


def calculate(n, nodes, nodeStatus):
    nodeMarks = [-1 for i in range(n)]

    q = deque()

    q.append((0, -1))

    while len(q) > 0:
        currentNode, parentNode = q.popleft()

        if nodeStatus[currentNode] == True:
            continue

        nodeStatus[currentNode] = True
        nodeMarks[currentNode] = parentNode
        childNodes = nodes[currentNode]

        for childNode in childNodes:
            q.append((childNode, currentNode))

    minusNumber = nodeMarks.count(-1)
    if minusNumber > 1:
        print("No")
        return

    print("Yes")
    for i in range(1, n):
        print(nodeMarks[i] + 1)


nodes, nodeStatus = prepare(N, M, ARR)

calculate(N, nodes, nodeStatus)
