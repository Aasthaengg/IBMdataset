import numpy as np
N = int(input())
h = np.array(list(map(int, input().split())))

from collections import deque
queue = deque([])

queue.append(h)

ans = 0

while(len(queue) > 0):
    new_h = queue.popleft()
    ans += np.min(new_h)
    new_h -= np.min(new_h)
    
    R = np.where(new_h == 0)[0][0]
    new_L = new_h[:R]
    new_R = new_h[R+1:]
    
    if new_L.size > 0:
        queue.append(new_L)
    if new_R.size > 0:
        queue.append(new_R)
    
print(ans)