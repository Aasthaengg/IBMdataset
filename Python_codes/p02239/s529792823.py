n = int(input())
G = [[] for i in range(n)] #G(i): 頂点iと隣接する頂点のlist
for i in range(n):
    a = [int(i) for i in input().split()]
    G[a[0]-1] = [i-1 for i in a[2:]]

d = [-1] * n
todo = [0]
d[0] = 0

while(todo != []):
    v = todo.pop(0)
    for i in G[v]:
        if d[i] == -1:
            d[i] = d[v]+1
            todo.append(i)

for i in range(n):
    print(i+1, d[i])
