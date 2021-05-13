# A - Darker and Darker
from collections import deque

H,W = map(int,input().split())
B = [[-1] * W for _ in range(H)]

queue = deque([])

for i in range(H):
    A = input()
    for j in range(W):
        if A[j]=='#':
            B[i][j] = 0
            queue.append((i,j))

ans = 0

while queue:
    I,J = queue.popleft()
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        i,j = I+di,J+dj
        if 0<=i<H and 0<=j<W:
            if B[i][j]<0:
                B[i][j] = B[I][J]+1
                ans = max(ans,B[i][j])
                queue.append((i,j))

print(ans)