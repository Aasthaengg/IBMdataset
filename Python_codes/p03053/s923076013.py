from collections import deque

def bfs(maze):
    h = len(maze)
    w = len(maze[0])
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    d = deque()
    
    last =[-1, -1]
    for y in range(h):
        for x in range(w):
            if maze[y][x] == '#':
                d.append([y, x])
                visited[y][x] = 0
                last[0] = y
                last[1] = x
    
    while d:
        y, x = d.popleft()
        
        for l, k in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            new_y, new_x = y + l, x + k
            
            if new_y < 0 or h <= new_y or new_x < 0 or w <= new_x:
                continue
            elif visited[new_y][new_x] != -1:
                continue
            elif maze[new_y][new_x] == '#':
                continue
            
            d.append([new_y, new_x])
            visited[new_y][new_x] = visited[y][x] + 1

        last[0] = y
        last[1] = x
        
    ''' 確認用
    print(last)
    for i in range(h):
        print(visited[i])
    '''
        
    return visited[last[0]][last[1]]

if __name__ == "__main__":
    h, w = map(int, input().split())
    maze = []
    for i in range(h):
        maze.append(list(input()))
    ''' 確認用
    for i in range(h):
        print(maze[i])
    '''
    
    print(bfs(maze))