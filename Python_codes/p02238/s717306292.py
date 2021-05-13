n = int(input())

adj = [0]*n # adjacent list

for i in range(n):
    tmp = list(map( int, input().split() ) )
    adj[tmp[0]-1] = list(map(lambda x : x - 1, tmp[2:]))

c = ['w']*n # color of each vertex
d = [0]*n # discovery time for each vertex
f = [0]*n  # finish time for each vertex
time = 0

def DFS_visit(u):
    global time
    time += 1
    d[u] = time
    c[u] = 'g'
    for v in adj[u]:
        if c[v] == 'w':
            DFS_visit(v)
    c[u] = 'b'
    time += 1
    f[u] = time
    
for u in range(n):
    if c[u] == 'w':
        DFS_visit(u)
        
        
for u in range(n):
    print(f"{u+1} {d[u]} {f[u]}")
