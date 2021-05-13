n,m = map(int,input().split())
l = [-1] + [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    l[a].append(b)
    l[b].append(a)
for mid in l[1]:
    if n in l[mid]:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')