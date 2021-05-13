import sys
from collections import deque

def input():
    return sys.stdin.readline().strip()

def main():
    H,W = map(int,input().split())
    A = [list(input()) for _ in range(H)]

    que = deque()
    for x in range(W):
        for y in range(H):
            if A[y][x] == '#':
                que.append((x,y,0))        
    ans = 0
    while que:
        x,y,c = que.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            sx = x + dx
            sy = y + dy
            if sx < 0 or sx >= W or sy < 0 or sy >= H or A[sy][sx] == '#':
                continue
            if A[sy][sx] == '.':
                que.append((sx,sy,c+1))
                A[sy][sx] = c + 1
                ans = max(ans,c+1)
    print(ans)

if __name__ == "__main__":
    main()