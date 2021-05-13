import sys
h, w = [int(x) for x in input().split()]
mat = [input() for _ in range(h)]
cnt = [[0] * w for _ in range(h)]
row_obs = [[-1] for _ in range(h)]
col_obs = [[-1] for _ in range(w)]

def main():
    for i, r in enumerate(mat):
        for j, c in enumerate(r):
            if c == '#':
                row_obs[i].append(j)
                col_obs[j].append(i)
        row_obs[i].append(w)
    for j in range(w):
        col_obs[j].append(h)

    for i in range(h):
        k = 0
        while True:
            prev, nxt = (row_obs[i][k], row_obs[i][k+1])
            for j in range(prev+1, nxt):
                    cnt[i][j] += nxt - prev - 1
            if nxt == w:
                break
            k += 1

    for j in range(w):
        k = 0
        while True:
            prev, nxt = (col_obs[j][k], col_obs[j][k+1])
            for i in range(prev+1, nxt):
                    cnt[i][j] += nxt - prev - 1
            if nxt == h:
                break
            k += 1

    ans = 0
    for i in range(h):
        for j in range(w):
            ans = max(ans, cnt[i][j] - 1)
    print(ans)

if __name__ == '__main__':
    main()