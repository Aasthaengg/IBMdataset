
import queue
h,w = map(int,input().split())

maze=[]

count_white=0

for i in range(h):
    maze_row = input()
    maze.append(maze_row)
    
    count_white+=maze_row.count(".")
    
dist = [ [-1]*w for i in range(h)]
goal = [w-1,h-1]
q=queue.Queue()
q.put((0,0,0))

moves = [[0,1], [1,0], [0,-1], [-1,0]]
dmax=-1
while not q.empty():
    
    x,y,d = q.get()
    
    if x==goal[0] and y==goal[1]:
        time=d
        dist[y][x]=d
        dmax=d
        break
    
    if dist[y][x] >= 0:
        continue
    
    else:
        
        dist[y][x]=d
        
        for dx,dy in moves:
            
            if 0<=x+dx<w and 0<=y+dy<h:
                if dist[y+dy][x+dx] == -1 and maze[y+dy][x+dx]!="#":
                
                    q.put((x+dx,y+dy,d+1))
if dmax!=-1:
    print(count_white-dmax-1)
    
else:
    print(-1)