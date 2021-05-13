#A
from collections import deque
H,W = map(int,input().split())
A = [list(str(input())) for h in range(H)]

C = [[-1 for w in range(W)] for h in range(H)]


start = deque([])
for h in range(H):
    for w in range(W):
        if A[h][w] == "#":
            start.append([h,w])
            C[h][w] = 0
            
while start:
    h,w = start.popleft()
    c_old = C[h][w]
    
    if h > 0:
        c_new = C[h-1][w]
        
        if c_new == -1:
            C[h-1][w] = c_old+1
            start.append([h-1,w])
            
    if w > 0:
        c_new = C[h][w-1]
        
        if c_new == -1:
            C[h][w-1] = c_old+1
            start.append([h,w-1])
            
    if w < W-1:
        c_new = C[h][w+1]
        
        if c_new == -1:
            C[h][w+1] = c_old+1
            start.append([h,w+1])
            
    if h < H-1:
        c_new = C[h+1][w]
        
        if c_new == -1:
            C[h+1][w] = c_old+1
            start.append([h+1,w])
            
            
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans,C[h][w])
        
        
print(ans)        
    


