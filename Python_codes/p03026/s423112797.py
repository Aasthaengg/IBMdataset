import sys
readline = sys.stdin.readline
write = sys.stdout.write

N = int(input())
edges = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int,readline().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
C = list(map(int, readline().split()))
C.sort()
print(str(sum(C)-C[-1]))

queue = [0]
D = ["x" for i in range(N)]
while queue:
    op = queue.pop(0)
    if D[op] != "x":
        continue
    D[op] = str(C.pop(-1))
    numchild = len(edges[op])
    for i in range(numchild):
        queue.append(edges[op][i])
print((' '.join(D)))