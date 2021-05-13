import sys
input = sys.stdin.readline  # NOQA

import numpy as np


def update_h_w(h, w, H, W):
    # -->
    if h % 2 == 0:
        if w == W - 1:
            h += 1
        else:
            w += 1
    # <--
    else:
        if w == 0:
            h += 1
        else:
            w -= 1
    return h, w


def main():
    H, W = map(int, input().split())
    a = np.zeros((H, W), dtype=int)
    for i in range(H):
        a[i] = list(map(int, input().split()))

    N = 0
    ans = []
    tmp = []
    h, w = 0, 0
    search_pair = False
    while h < H:
        if search_pair:
            tmp.append((h + 1, w + 1))
            if a[h, w] % 2 == 1:
                search_pair = False
                ans.append(tmp)
                N += len(tmp) - 1
                tmp = []
        else:
            if a[h, w] % 2 == 1:
                search_pair = True
                tmp.append((h + 1, w + 1))
        h, w = update_h_w(h, w, H, W)

    print(N)
    for p in ans:
        for i in range(len(p) - 1):
            print(" ".join(map(str, (p[i][0], p[i][1], p[i+1][0], p[i+1][1]))))


if __name__ == "__main__":
    main()
