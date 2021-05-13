import sys
from collections import deque

input = sys.stdin.readline
digtmp = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def flatten_2dim(array):
    return [item for sublist in array for item in sublist]

def main():
    H, W = map(int, input().split())
    grid = []; black = deque([])
    grid.append([0]*(W+2))
    for i in range(H):
        tmp = list(input()[:-1])
        for j in range(W):
            if tmp[j] == '#':
                black.append((i+1, j+1))
                tmp[j] = 0
        grid.append([0] + tmp + [0])
    grid.append([0]*(W+2))

    for _ in range(pow(10, 6)):
        fr = black.popleft()
        gfr = grid[fr[0]][fr[1]]
        for d in digtmp:
            to = (fr[0]+d[0], fr[1]+d[1])
            gto = grid[to[0]][to[1]]
            if gto == '.':
                grid[to[0]][to[1]] = gfr + 1
                black.append(to)
            elif gto != '#':
                if gfr + 1 < gto:
                    grid[to[0]][to[1]] = gfr + 1
                    black.append(to)
            else:
                pass
        if len(black) == 0:
            break
    
    ans = max(flatten_2dim(grid))
    print(ans)

if __name__ == "__main__":
    main()
