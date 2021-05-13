from collections import deque
n = int(input())

Map = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    Map[a-1].append(b-1)
    Map[b-1].append(a-1)
INF = float('inf')
def distance(st):
    d = [INF for i in range(n)]
    d[st] = 0
    q = deque()
    q.append(st)
    while q:
        index = q.pop()
        for nexts in Map[index]:
            if d[nexts] == INF:
                d[nexts] = d[index]+1
                q.append(nexts)
    return d
d1 = distance(0)
d2 = distance(n-1)

fen = 0
snu = 0
for i in range(n):
    if d1[i]<= d2[i]:
        fen += 1
    else:
        snu += 1

if fen>snu:
    print('Fennec')
else:
    print('Snuke')