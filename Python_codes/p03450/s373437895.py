n,m = map(int, input().split())

dist = [[] for i in range(n)]

for i in range(m):
    l,r,d = map(int,input().split())
    l-=1
    r-=1
    dist[l].append([r,d])
    dist[r].append([l,-d])


position = [10**10]*n
for i in range(n):
    if position[i]==10**10:
        stack = [i]
        position[i] = 0
        while stack:
            p = stack.pop()
            for to,d in dist[p]:
                if position[to]==10**10:
                    position[to]=position[p]+d
                    stack.append(to)

for i in range(n):
    for to,d in dist[i]:
        if position[to]-position[i]!=d:
            print('No')
            exit()
print('Yes')


