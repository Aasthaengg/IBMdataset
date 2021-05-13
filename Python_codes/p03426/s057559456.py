def main():
    import sys
    input = sys.stdin.buffer.readline
    H, W, D = (int(i) for i in input().split())
    A = [[int(i) for i in input().split()] for j in range(H)]
    Q = int(input())
    LR = [[int(i) for i in input().split()] for j in range(Q)]

    B = [0]*(H*W+1)
    pos = {A[i][j]: (i+1, j+1) for i in range(H) for j in range(W)}

    for i in range(D+1, H*W+1):
        y, x = pos[i - D]
        ny, nx = pos[i]
        power = abs(nx - x) + abs(ny - y)
        B[i] = B[i - D] + power

    for le, ri in LR:
        print(B[ri] - B[le])


if __name__ == '__main__':
    main()
