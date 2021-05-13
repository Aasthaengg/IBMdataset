n = int(input())
graph = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
L = list(map(int,input().split()))
L.sort()
used = [0]*n
ans = [0]*n
used[0] = 1
ans[0] = L[n-1]
next = graph[0]
cur = n-2
while len(next) > 0:
    t = next.pop()
    ans[t] = L[cur]
    cur -= 1
    used[t] = 1
    for i in range(len(graph[t])):
        if used[graph[t][i]] != 1:
            next.append(graph[t][i])
print(sum(L)-L[n-1])
print(' '.join(map(str,ans)))
