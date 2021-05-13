import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    H,W = LI()
    M = [sys.stdin.readline().rstrip() for _ in range(H)]

    c = [[0] * W for _ in range(H)]
    q = collections.deque()
    ans = 0
    for i in range(H):
        for j in range(W):
            if c[i][j]: continue

            black = 0; white = 0
            q.append((i,j,M[i][j]))
            c[i][j] = 1
            while q:
                y,x,s = q.popleft()
                if s == '#': black += 1
                else: white += 1
                for dy,dx in ((0,1),(1,0),(0,-1),(-1,0)):
                    if 0 <= y+dy < H and 0 <= x+dx < W:
                        if c[y+dy][x+dx] or M[y+dy][x+dx] == s: continue
                        c[y+dy][x+dx] = 1
                        q.append((y+dy,x+dx,M[y+dy][x+dx]))
            ans += black * white
    print(ans)


if __name__ == '__main__':
    main()