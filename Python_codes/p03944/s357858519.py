#!/usr/bin/env python3
import sys
def input():
    return sys.stdin.readline()[:-1]

def main():
    W, H, N = map(int, input().split())
    x = [0] * N
    y = [0] * N
    a = [0] * N
    for i in range(N):
        x[i], y[i], a[i] = map(int, input().split())

    lx = 0
    rx = W
    uy = H
    dy = 0
    for i in range(N):
        if a[i] == 1:
            lx = max(lx, x[i])
        if a[i] == 2:
            rx = min(rx, x[i])
        if a[i] == 3:
            dy = max(dy, y[i])
        if a[i] == 4:
            uy = min(uy, y[i])
    X = rx - lx
    Y = uy - dy
    ans = X * Y
    if X < 0 or Y < 0:
        ans = 0
    print(ans)

if __name__ == '__main__':
    main()
