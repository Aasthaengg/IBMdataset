N,u,v = map(int, input().split())
if u == v:
  print(0)
  exit()
  
ver= [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    ver[a-1].append(b-1)
    ver[b-1].append(a-1)
    
    
def bfs(start):
    dist_turn = [float('inf') for i in range(N)]
    dist_turn[start] = 0
    visited = set()
    visited.add(start)
    turn = 0
    prev_dists = [start]
    new_dists = []
    while len(prev_dists) != 0:
        turn += 1
        for prev_dist in prev_dists:
            for new_dist in ver[prev_dist]: 
                if new_dist not  in visited:
                    visited.add(new_dist)
                    new_dists.append(new_dist)
                    dist_turn[new_dist] = turn
        prev_dists = new_dists
        new_dists = []
    return dist_turn

u_shortest = bfs(u-1)
v_shortest = bfs(v-1)

max_dist = -1
for i in range(N):
    if u_shortest[i] < v_shortest[i]:
        max_dist = max(max_dist, v_shortest[i])
print(max_dist - 1)