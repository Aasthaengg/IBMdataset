import copy
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append([c,b-1])
    graph[b-1].append([c,a-1])
q,k = map(int,input().split())
wait = [k-1]
d = [0]*n
done = [False]*n
while wait:
    nxt = []
    for i in wait:
        for l in graph[i]:
            if not done[l[1]]:
                done[l[1]] = True
                d[l[1]] = d[i] + l[0]
                nxt.append(l[1])
    wait = copy.copy(nxt)


for i in range(q):
    x,y = map(int,input().split())
    print(d[y-1]+d[x-1])