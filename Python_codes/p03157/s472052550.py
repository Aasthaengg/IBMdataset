def aising19_c():
    from collections import deque

    h, w = (int(x) for x in input().split())
    color = [[s == '#' for s in str(input())] for _ in range(h)]
    used = [[False]*w for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if used[i][j]: continue
            bk, wt = 0, 0
            que = deque()
            used[i][j] = True
            que.append((i, j))
            while que:
                ci, cj = que.popleft()
                if color[ci][cj]: bk += 1
                else: wt += 1
                for di, dj in ((-1,0),(0,-1),(0,1),(1,0)):
                    ni, nj = ci+di, cj+dj
                    if ni < 0 or h <= ni or nj < 0 or w <= nj: continue
                    if color[ci][cj] == color[ni][nj]: continue
                    if used[ni][nj]: continue
                    used[ni][nj] = True
                    que.append((ni, nj))
            ans += bk * wt
    print(ans)

if __name__ == '__main__':
    aising19_c()