import sys
input = sys.stdin.readline
from collections import deque


def read():
    H, W, K = list(map(int, input().strip().split()))
    S = []
    for i in range(H):
        s = list(input().strip())
        S.append(s)
    return H, W, K, S


def paint(row, l, r, uid):
    for i in range(l, r):
        row[i] = str(uid)


def copy_row(src, dst, W):
    for i in range(W):
        dst[i] = src[i]


def solve(H, W, K, S):
    uid = 0
    for i in range(H):
        l = 0
        for j in range(W):
            r = j+1
            if S[i][j] == "#":
                uid += 1
                paint(S[i], l, r, uid)
                l = r
        if l > 0:
            r = W
            paint(S[i], l, r, uid)
            h = 0
    
    # fill empty rows
    non_empty_row = -1
    for i in range(H):
        if S[i][0] != ".":
            non_empty_row = i
        elif non_empty_row >= 0 and S[i][0] == ".":
            copy_row(S[non_empty_row], S[i], W)

    for i in range(H-1, -1, -1):
        if S[i][0] != ".":
            non_empty_row = i
        elif non_empty_row >= 0 and S[i][0] == ".":
            copy_row(S[non_empty_row], S[i], W)

    for i in range(H):
        print(" ".join(S[i]))


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
