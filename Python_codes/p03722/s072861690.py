from collections import deque
n,m = map(int,input().split())
e1 = [[] for i in range(n)]
e2 = [[] for i in range(n)]
l = []
for i in range(m):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    e1[a].append(b)
    e2[b].append(a)
    l.append([a,b,c])

def search(x,e):
    dis = [0]*n
    dis[x] = 1
    q = deque([])
    q.append(x)
    while q:
        now = q.popleft()
        for nex in e[now]:
            if dis[nex] == 0:
                dis[nex] = 1
                q.append(nex)

    return dis

dis1 = search(0,e1)
dis2 = search(n-1,e2)
dis = [0]*n
for i in range(n):
    if dis1[i] == 1 and dis2[i] == 1:
        dis[i] = 1

li = []
for i in range(m):
    a,b,c = l[i]
    if dis[a] == 1 and dis[b] == 1:
        li.append(l[i])

ans = [-float("INF")]*n
ans[0] = 0

for i in range(n):

    check = False
    for i,j,k in li:
        if ans[i]+k > ans[j]:
            ans[j] = ans[i]+k
            check = True
    
    if not check:
        print(ans[-1])
        exit()
print("inf")