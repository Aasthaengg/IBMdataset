from collections import defaultdict, deque

N, M = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(M)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1
length=defaultdict(int)

q = deque(set(i for i in range(1,N+1))-set(ins.keys()))
length=defaultdict(int)
while q:
    v1 = q.popleft()
    for v2 in outs[v1]:
        ins[v2] -= 1
        if length[v2]<=length[v1]:
            length[v2]=length[v1]+1
        if ins[v2] == 0:
            q.append(v2)

print(max(length.values()))