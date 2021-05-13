import numpy as np

h , w = map(int, input().split())
visited = np.zeros((h,w),dtype=int)

for y in range(h):
    _in = input()
    for x, value in enumerate(_in):
        if value == '.':
            visited[y][x] = 10**9
            
for i in range(1,h):
    visited[i,:] = np.minimum(visited[i,:],visited[i-1,:]+1)
for i in reversed(range(h-1)):
    visited[i,:] = np.minimum(visited[i,:],visited[i+1,:]+1)
for j in range(1,w):
    visited[:,j] = np.minimum(visited[:,j],visited[:,j-1]+1)
for j in reversed(range(w-1)):
    visited[:,j] = np.minimum(visited[:,j],visited[:,j+1]+1)
print(np.max(visited))