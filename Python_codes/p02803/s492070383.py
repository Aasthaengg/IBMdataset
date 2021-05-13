from collections import deque
import copy

digtmp = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(maze, s):
    que = deque([s])
    maze[s[0]][s[1]] = 0
    ans = 0
    for _ in range(pow(10, 3)):
        fr = que.popleft()
        for d in digtmp:
            to = [fr[0] + d[0], fr[1] + d[1]]
            if maze[to[0]][to[1]] == '.':
                nxt = maze[fr[0]][fr[1]] + 1
                maze[to[0]][to[1]] = nxt
                ans = max(ans, nxt)
                que.append(to)
        if len(que) == 0:
            break
    return ans

def main():
    H, W = map(int, input().split())
    grid = []; road = []
    grid.append(['#']*(W+2))
    for i in range(H):
        tmp = list(input())
        for j in range(W):
            if tmp[j] == '.':
                road.append([i+1, j+1])
        grid.append(['#'] + tmp + ['#'])
    grid.append(['#']*(W+2))
    
    ans = 1
    for r in road:
        maze = copy.deepcopy(grid)
        ans = max(ans, bfs(maze, r))
    print(ans)

if __name__ == "__main__":
    main()
