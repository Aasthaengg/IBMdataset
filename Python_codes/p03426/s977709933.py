#!/usr/bin/env python3

def main():
    h, w, d = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(h)]
    loc = [None for i in range(h * w + 1)]
    for i in range(h):
        for j in range(w):
            loc[a[i][j]] = (i, j)

    f = [None for i in range(h * w + 1)]
    for x0 in range(h * w):
        x1 = x0 + 1
        if x1 <= d:
            f[x1] = 0
        else:
            r1, l1 = loc[x1]
            r2, l2 = loc[x1 - d]
            f[x1] = f[x1 - d] + abs(r1 - r2) + abs(l1 - l2)

    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(f[r] - f[l])

if __name__ == "__main__":
    main()
