import sys
 
from collections import deque
 
def LI():
	return [ int(s) for s in input().split() ]
 
N,K =LI()
tree = {}
for i in range(N):
  tree[i] = []
 
MOD = (10**9)+7
color = K
 
for _ in range(N-1):
    a,b = LI()
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    
 
## bfs ###
search_candidate = deque([0])
visited = [False]*N
hierarchy = [-1]*N
hierarchy[0] = 1
for t in tree[0]:
    if t != 0:
        hierarchy[t] = 2

while search_candidate:
    search = search_candidate.popleft()
    if hierarchy[search] == 1:
        cnt = K - 1
    else:
        cnt = K - 2
    visited[search] = True
    
    for child in tree[search]:
        if visited[child]:
            continue 
 
        if cnt <= 0:
            print(0)
            sys.exit()
 
        color = (color*cnt) % MOD
        cnt -= 1
        search_candidate.appendleft(child)
      
print(color)