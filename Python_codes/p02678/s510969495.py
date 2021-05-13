import queue

n, m = map(int, input().split())
maze = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    maze[a-1].append(b-1)
    maze[b-1].append(a-1)

ans = [-1 for _ in range(n)]
ans[0] = 0
q = queue.Queue()
q.put(0)
while not q.empty():
    start = q.get()
    for end in maze[start]:
        if ans[end] == -1:
            q.put(end)
            ans[end] = start

if -1 in ans[1:]:
    print('No')
else:
    print('Yes')
    for i in range(1,n):
        print(ans[i]+1)
