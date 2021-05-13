n, m = map(int,input().split())

edge = [[] for i in range(n)]

for i in range(m):
    a, b = map(lambda x:int(x)-1,input().split())
    edge[a].append(b)

possible = False
for to in edge[0]:
    if n-1 in edge[to]:
        possible = True
        break

print("POSSIBLE" if possible else "IMPOSSIBLE")