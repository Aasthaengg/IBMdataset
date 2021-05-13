from collections import deque

def cal():
    h, w = map(int, input().split())
    q = deque()
    counts = [[True for _ in range(w+2)]]+[[True]+[False]*w+[True] for _ in range(h)]+[[True for _ in range(w+2)]]
    for i in range(h):
        a = input()
        for j in range(w):
            if a[j] == '#':
                q.append([i+1, j+1, 0])
                counts[i+1][j+1] = True

    while q:
        x, y, z = q.popleft()    
        if not counts[x+1][y]:
            counts[x+1][y] = True
            q.append([x+1, y, z+1])
        if not counts[x-1][y]:
            counts[x-1][y] = True
            q.append([x-1, y, z+1])
        if not counts[x][y+1]:
            counts[x][y+1] = True
            q.append([x, y+1, z+1])
        if not counts[x][y-1]:
            counts[x][y-1] = True
            q.append([x, y-1, z+1])
    print(z)
    

cal()
