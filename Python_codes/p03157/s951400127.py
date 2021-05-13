from collections import deque

h,w = map(int,input().split())

s = [0]*(h+2)
for i in range(1,h+1):
    s[i] = [0] + list(input()) + [0]
s[0] = [0]*(w+2)
s[-1] = [0]*(w+2)

reach = [[-1 for j in range(w+2)] for i in range(h+2)]
lis = []

for i in range(1,h+1):
    for j in range(1,w+1):
        if reach == 0:
            pass
        else:
            black = 0
            white = 0
            if s[i][j] == "#":
                state = 1
                black += 1
            else:
                state = 0
                white += 1
                
            q = deque()
            q.append([i,j,state])
            reach[i][j] = 0
            
            while q:
                [x,y,state] = q.popleft()
                
                if reach[x-1][y] == -1:
                    if state == 0 and s[x-1][y] == "#":
                        reach[x-1][y] = 0
                        q.append([x-1, y ,1])
                        black += 1
                    elif  state == 1 and s[x-1][y] == ".":
                        reach[x-1][y] = 0
                        q.append([x-1, y ,0])
                        white += 1
                
                if reach[x+1][y] == -1:
                    if state == 0 and s[x+1][y] == "#":
                        reach[x+1][y] = 0
                        q.append([x+1, y ,1])
                        black += 1
                    elif  state == 1 and s[x+1][y] == ".":
                        reach[x+1][y] = 0
                        q.append([x+1, y ,0])
                        white += 1
                        
                if reach[x][y-1] == -1:
                    if state == 0 and s[x][y-1] == "#":
                        reach[x][y-1] = 0
                        q.append([x, y-1 ,1])
                        black += 1
                    elif  state == 1 and s[x][y-1] == ".":
                        reach[x][y-1] = 0
                        q.append([x, y-1 ,0])
                        white += 1
                    
                if reach[x][y+1] == -1:
                    if state == 0 and s[x][y+1] == "#":
                        reach[x][y+1] = 0
                        q.append([x, y+1 ,1])
                        black += 1
                    elif  state == 1 and s[x][y+1] == ".":
                        reach[x][y+1] = 0
                        q.append([x, y+1 ,0])
                        white += 1
                
            lis.append([black,white])
ans = 0
for s,t in lis:
    ans += s*t
print(ans)