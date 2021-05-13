import sys
INF = 10 ** 9
n, m = [int(i) for i in sys.stdin.readline().split()]
graph = {j:[] for j in range(3 * n)}
for i in range(m):
    u, v = [int(i) for i in sys.stdin.readline().split()]
    u -= 1
    v -= 1
    graph[u].append(n+v)
    graph[u+n].append(2*n+v)
    graph[u + 2 * n].append(v)
s, t = [int(i) for i in sys.stdin.readline().split()]
s -= 1
t -= 1

que = [s]
flg = False
already = set()
dist = [INF for i in range(3 * n)]
dist[s] = 0
while que:
    cur= que[0]
    que.pop(0)
    for i in graph[cur]:
        if i not in already:
            if i == t:
                res = dist[cur] + 1
                que.clear()
                flg = True
                break
            que.append(i)
            dist[i] = dist[cur] + 1
            already.add(i)
if not flg:
    res = -1
else:
    res //= 3

print(res)