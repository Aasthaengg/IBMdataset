def main():
    import sys
    from collections import deque

    def input(): return sys.stdin.readline().rstrip()

    def bfs(si, sj):
        di = [-1, 0, 1, 0]
        dj = [0, 1, 0, -1]
        que = deque([(si, sj)])
        dist[0][0] = 0
        while que:
            i, j = que.popleft()
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if (ni < 0 or ni >= h or nj < 0 or nj >= w):
                    continue
                if g[ni][nj] == '#':
                    continue
                if dist[ni][nj] > dist[i][j]+1:
                    dist[ni][nj] = dist[i][j]+1
                    que.append((ni, nj))
        

    h, w = map(int, input().split())
    g = []
    cnt = 0
    for i in range(h):
        g.append(input())
        cnt += g[-1].count('#')
    inf = 10**6
    dist = [[inf]*w for _ in range(h)]

    bfs(0, 0)
    if dist[-1][-1] == inf:
        print(-1)
    else:
        ans = h*w-cnt-dist[-1][-1]-1
        print(ans)

if __name__ == '__main__':
    main()