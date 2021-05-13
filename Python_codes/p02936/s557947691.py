import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
n,q = map(int,readline().split())
ABPX = list(map(int,read().split()))
AB = iter(ABPX[:n+n-2])
PX = iter(ABPX[n+n-2:])

graph = [[] for _ in range(n+1)]
for a, b in zip(AB, AB):
    graph[a].append(b)
    graph[b].append(a)

val = [0] * (n+1)
for p, x in zip(PX, PX):
    val[p] += x

stack = [1] #queue的なやつ
parent = [0] * (n+1)
while stack:
    x = stack.pop() #根を引っこ抜く
    for y in graph[x]: #木を見る
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)
        val[y] += val[x]
        
print(' '.join(map(str, val[1:])))