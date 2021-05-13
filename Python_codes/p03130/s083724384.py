from collections import defaultdict,deque

N = 4
d = defaultdict(list)
for i in range(3):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)


for i in range(1,5):
    dist = [None]*N
    q = deque()
    s = i  # スタート
    q.append(s)
    dist[s-1] = 0

    while len(q)!=0:
        From = q.popleft()
        for To in d[From]:
            if dist[To-1] == None:
                q.append(To)
                dist[To-1] = dist[From-1]+1
    if set(dist)=={0,1,2,3}:
        print("YES")
        exit()
print("NO")