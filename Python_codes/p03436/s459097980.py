import collections
 
H,W = list(map(int,input().split()))
S = [list(input()) for _ in range(H)]
copyS = [S[i][:] for i in range(H)]
que = collections.deque()
que.append([0,0])
 
d = [[float('inf') for _ in range(W)] for _ in range(H)]
d[0][0] = 0
S[0][0] = '#'
 
while len(que) != 0:
    y,x = que.popleft()
    if y == H-1 and x == W-1:
        break
    for direct in [[1,0],[-1,0],[0,1],[0,-1]]:
        if 0 <= y+direct[0] <= H-1 and 0 <= x+direct[1] <= W-1:
            if S[y+direct[0]][x+direct[1]] != '#':
                d[y+direct[0]][x+direct[1]] = d[y][x]+1
                S[y+direct[0]][x+direct[1]] = '#'
                que.append([y+direct[0], x+direct[1]])

if y != H-1 or x != W-1:
    print(-1)
    exit()

count = 0
for i in range(H):
    for j in range(W):
        if copyS[i][j] == '.':
            count += 1
print(count - (d[y][x]+1))