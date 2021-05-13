n,m = map(int,input().split())
path = []
for i in range(n+1):
    path.append([])
for i in range(m):
    a,b = map(int,input().split())
    path[a].append(b)
    path[b].append(a)
for i in range(1,n+1):
    print(len(path[i]))
