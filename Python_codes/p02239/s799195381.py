from collections import deque

#キューを使った幅優先探索の実装
l = int(input())
rlist = []
for i in range(l):
    li = list(map(int, input().split()))
    rlist.append(deque([ll-1 for ll in li[2:]]))


color = ['white'] * l
queue = deque([])
d = [10000000] * l

def bfs(u):
    color[u] = 'gray'
    d[u] = 0
    queue.append(u)

    while(len(queue) > 0):
        u = queue.popleft()
        for rl in rlist[u]:
            if color[rl] == 'white':
                color[rl] = 'gray'
                d[rl] = d[u] + 1
                queue.append(rl)
        color[u] = 'black'

bfs(0)

for i in range(l):
    if d[i] == 10000000:
        d[i] = -1

for i in range(l):
    print(str(i+1) + ' ' + str(d[i]))
