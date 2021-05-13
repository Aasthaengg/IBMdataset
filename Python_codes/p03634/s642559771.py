N = int(input())
INF = float('inf')
edges = [[] for i in range(N+1)]
for i in range(N-1):
    a,b,c = list(map(int,input().split()))
    edges[a].append((b,c))
    edges[b].append((a,c))

Q,K = list(map(int,input().split()))
checked = [0]*(N+1)
checked[K] = 1
stack = [K]
distances_from_K = [-1]*(N+1)
distances_from_K[K] = 0
while stack:
    s = stack.pop()
    for t in edges[s]:
        if not checked[t[0]]:
            checked[t[0]] = 1
            distances_from_K[t[0]] = distances_from_K[s] + t[1]
            stack.append(t[0])

for i in range(Q):
    x,y = list(map(int,input().split()))
    print(distances_from_K[x]+distances_from_K[y])