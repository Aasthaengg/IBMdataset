from collections import deque
h,w = map(int,input().split())
map_input = [list(input()) for i in range(h)]

queue = deque([])
for i in range(h):
    for j in range(w):
        if map_input[i][j]=='#':
            queue.append([j,i])

mx = [0,0,1,-1]
my = [1,-1,0,0]

ans = -1
def bfs(map_input,queue,ans):
    while queue:
        queue2 = deque([])
        ans+=1
        for x,y in queue:
            for i in range(4):
                nx = x+mx[i]
                ny = y+my[i]
                if 0<=nx<w and 0<=ny<h:
                    if map_input[ny][nx]=='#':
                        continue
                    map_input[ny][nx]='#'
                    queue2.append([nx,ny])

        queue = queue2
    return ans

ans = bfs(map_input,queue,ans)
print(ans)