def main():
    import sys
    input = sys.stdin.buffer.readline
    H, W, D = (int(i) for i in input().split())
    A = [[int(i) for i in input().split()] for j in range(H)]
    Q = int(input())
    LR = [[int(i) for i in input().split()] for j in range(Q)]
    B = [10**9]*(H*W+1)
    pos = {A[i][j]: (i+1, j+1) for i in range(H) for j in range(W)}
    for i in range(1, H*W+1):
        cur_p = i
        if B[cur_p] < 10**9:
            continue
        B[cur_p] = 0
        y, x = pos[cur_p]
        while cur_p + D <= H*W:
            np = cur_p + D
            ny, nx = pos[np]
            power = abs(nx - x) + abs(ny - y)
            B[np] = B[cur_p] + power
            cur_p = np
            y, x = ny, nx

    for le, ri in LR:
        print(B[ri] - B[le])


if __name__ == '__main__':
    main()
