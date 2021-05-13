from collections import deque
from typing import List


def main():
    h, w = map(int, input().split())
    g = []
    for _ in range(h):
        r = list(input())
        g.append(r)
    print(mm(h, w, g))


def mm(h: int, w: int, g: List[List[str]]) -> int:
    ret = 0
    for i in range(h):
        for j in range(w):
            if (g[i][j] == '#'):
                continue
            q = deque([(i, j, 0)])
            v = [[0] * w for _ in range(h)]
            v[i][j] = 1
            while q:
                ii, jj, cnt = q.popleft()
                ret = max(ret, cnt)
                # ↓
                if ii < h - 1 and g[ii + 1][jj] == '.' and v[ii + 1][jj] == 0:
                    v[ii + 1][jj] = 1
                    q.append((ii + 1, jj, cnt + 1))
                # →
                if jj < w - 1 and g[ii][jj + 1] == '.' and v[ii][jj + 1] == 0:
                    v[ii][jj + 1] = 1
                    q.append((ii, jj + 1, cnt + 1))
                # ↑
                if ii > 0 and g[ii - 1][jj] == '.' and v[ii - 1][jj] == 0:
                    v[ii - 1][jj] = 1
                    q.append((ii - 1, jj, cnt + 1))
                # ←
                if jj > 0 and g[ii][jj - 1] == '.' and v[ii][jj - 1] == 0:
                    v[ii][jj - 1] = 1
                    q.append((ii, jj - 1, cnt + 1))
    return ret


if __name__ == '__main__':
    main()
