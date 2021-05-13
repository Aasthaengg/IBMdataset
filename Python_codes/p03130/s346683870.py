graph = [[]for _ in range(4)]
for i in range(3):
    a,b = map(int,input().split())
    a-= 1
    b-= 1
    graph[a].append(b)
    graph[b].append(a)
maxa = 0
for i in range(4):
    maxa = max(len(graph[i]),maxa)

if maxa == 3:
    print("NO")
    exit(0)
print("YES")
