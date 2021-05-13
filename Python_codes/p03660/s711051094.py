n = int(input())
edge = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)
visited = [0]*n
visited[0] = 1
visited[n-1] = 1
visited_all = [1]*n
nextF = edge[0]
nextS = edge[n-1]
black = 1
white = 1
while visited != visited_all:
    l = []
    for f in nextF:
        if visited[f] == 0:
            visited[f] = 1
            black += 1
            for x in edge[f]:
                l.append(x)
            nextF = l
    l = []
    for s in nextS:
        if visited[s] == 0:
            visited[s] = 1
            white += 1
            for y in edge[s]:
                l.append(y)
            nextS = l
if black > white:
    print('Fennec')
else:
    print('Snuke')