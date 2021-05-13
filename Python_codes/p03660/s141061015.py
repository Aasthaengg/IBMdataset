from collections import deque
N = int(input())
path = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    path[a-1].append(b-1)
    path[b-1].append(a-1)

steps = [-99 for _ in range(N)]
steps[0] = 0
isVisited = [False for _ in range(N)]
toSearch = deque([0, ])
isVisited[0] = True
while len(toSearch) > 0:
    nowP = toSearch.pop()
    nowStep = steps[nowP]
    if nowP == N-1:
        break
    for nextP in path[nowP]:
        if not isVisited[nextP]:
            isVisited[nextP] = True
            toSearch.appendleft(nextP)
            steps[nextP] = nowStep + 1

fennecLength = ((nowStep-1)+1)//2

snukePoint = 0
isVisited = [False for _ in range(N)]
toSearch = deque([N-1, ])
isVisited[N-1] = True
while len(toSearch) > 0:
    nowP = toSearch.pop()
    snukePoint += 1
    nowStep = steps[nowP]
    # To FIX break condition
    if nowStep == fennecLength:
        snukePoint -= 1
        continue
    for nextP in path[nowP]:
        if not isVisited[nextP]:
            isVisited[nextP] = True
            toSearch.appendleft(nextP)
if snukePoint >= (N+1)//2:
    print("Snuke")
else:
    print("Fennec")
#print(snukePoint)
#print(steps)