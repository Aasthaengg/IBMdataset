import queue
n = int(input())

g = {}
for i in range(n):
    x = list(map(int, input().split()))
    g[x[0]] = [x[2:], 'w', x[0], None]

q = queue.Queue()
node = g[1]
node[-1] = 0
node[1] = 'g'
q.put(node)

while not q.empty():
    node  = q.get()
    d = node[-1] + 1
    for i in node[0]:
        ch = g[i]
        if ch[1] == 'w':
            ch[-1] = d
            ch[1] = 'g'
            q.put(ch)

for i in range(n):
    node = g[i+1]
    if node[-1] == None:
        d = -1
    else:
        d = node[-1]
    print("{} {}".format(i+1, d))