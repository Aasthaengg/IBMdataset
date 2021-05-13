import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15
Dy = (-1,0,1,0)
Dx = (0,1,0,-1)
def main():
    H,W = map(int,input().split())
    grid = [input() for _ in range(H)]
    grid = [[1 if g == '#' else 0 for g in gr] for gr in grid]
    G = [[] for _ in range(H*W)]

    for i in range(H):
        for j in range(W):
            for dy,dx in zip(Dy,Dx):
                y = i + dy
                x = j + dx
                if y < 0 or y >= H or x < 0 or x >= W:
                    continue
                if grid[i][j]^grid[y][x] == 1:
                    G[i*W + j].append(y*W + x)
                    G[y*W + x].append(i*W + j)
    
    visited = [-1] * (H*W)
    ans = 0
    for i in range(W*H):
        if visited[i] >= 0:
            continue
        stack = [i]
        visited[i] = 0
        w = 1
        b = 0
        while stack:
            v = stack.pop()
            for e in G[v]:
                if visited[e] >= 0:
                    continue
                visited[e] = visited[v]^1
                if visited[e] == 1:
                    b += 1
                else:
                    w += 1
                stack.append(e)
        ans += b*w
    print(ans)
if __name__ == '__main__':
    main()