import queue

N, K = map(int, input().split())
P = list(map(lambda v: v-1, map(int, input().split())))
C = list(map(int, input().split()))

visited = [False] * N
q = queue.Queue()
lists = list()

for i in range(N):
    q.put(dict(index=i, l=None))
    while not q.empty():
        d = q.get()
        if visited[d['index']]:
            continue
        visited[d['index']] = True
        l = d['l']
        if l is None:
            l = list()
            lists.append(l)
        l.append(C[d['index']])
        q.put(dict(index=P[d['index']], l=l))

maxv = -float('inf')

for l in lists:
    summ = sum(l)
    if summ > 0:
        score = summ * (K//len(l))
        rest = K % len(l)
        if rest == 0:
            score -= summ
            rest = len(l)
        for i in range(len(l)):
            v = 0
            for j in range(rest):
                v += l[i+j if i+j < len(l) else i+j-len(l)]
                maxv = max(maxv, score+v)
    else:
        for i in range(len(l)):
            v = 0
            for j in range(len(l)):
                v += l[i+j if i+j < len(l) else i+j-len(l)]
                maxv = max(maxv, v)
print(maxv)
