import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    sys.setrecursionlimit(10**7)
    INF = 10**18
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    H,W = LI()
    f = [[0] * W for _ in range(H)]
    q = collections.deque()
    for i in range(H):
        for j,x in enumerate(sys.stdin.readline().rstrip()):
            if x == '#':
                f[i][j] = 1
                q.append((i,j,0))
    ans = 0
    while q:
        y,x,c = q.popleft()
        ans = max(ans,c)
        for dy,dx in ((0,1),(1,0),(-1,0),(0,-1)):
            if 0 <= x+dx < W and 0 <= y+dy < H:
                if f[y+dy][x+dx] == 0:
                    f[y+dy][x+dx] = 1
                    q.append((y+dy,x+dx,c+1))
    print(ans)

if __name__ == '__main__':
    main()