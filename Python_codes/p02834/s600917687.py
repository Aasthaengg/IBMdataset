n,u,v = list(map(int,input().split()))

graph = [[] for i in range(n)]

for i in range(n-1):
    a,b = list(map(int,input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

stack = [u-1]
check = [False]*n
check[u-1] = True
check[v-1] = True
takahasi = [0]*n

while stack:
    now = stack.pop()
    for i in range(len(graph[now])):
        if check[graph[now][i]]:continue
        check[graph[now][i]] = True
        stack.append(graph[now][i])
        takahasi[graph[now][i]] = 1 + takahasi[now]

aoki = [0]*n
stack = [v-1]
check = [False]*n
check[v-1] = True
while stack:
    now = stack.pop()
    for i in range(len(graph[now])):
        if check[graph[now][i]]:continue
        check[graph[now][i]] = True
        stack.append(graph[now][i])
        aoki[graph[now][i]] = 1 + aoki[now]

#print(takahasi)
#print(aoki)

ans = 0
ans_= n+1
takahasi[u-1] = -1

henone = [0]*n
for i in range(n):
    if len(graph[i]) == 1:
        henone[i] = 1

for i in range(n):
    if henone[i] == 1 and takahasi[i] != 0 and takahasi[i] < aoki[i]:
        ans = max(aoki[i]-1,ans)
    """
    if takahasi[i] == 0:continue
    if takahasi[i] < aoki[i]:
        if (aoki[i] - takahasi[i]) % 2 == 1:
            ans = max(ans,aoki[i]-1)
        else:
            ans = max(ans,aoki[i])
    elif takahasi[i] == aoki[i]:
        ans_ = min(ans_,takahasi[i])
    """
print(ans)