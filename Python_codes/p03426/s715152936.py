def main():
    import sys
    input = sys.stdin.buffer.readline
    read = sys.stdin.buffer.read
    H, W, D = (int(i) for i in input().split())
    R = [r for r in read().rstrip().split(b'\n')]
    A = [[int(i) for i in r.split()] for r in R[:H]]

    B = [0]*(H*W+1)
    pos = {A[i][j]: (i+1, j+1) for i in range(H) for j in range(W)}

    for i in range(D+1, H*W+1):
        y, x = pos[i - D]
        ny, nx = pos[i]
        power = abs(nx - x) + abs(ny - y)
        B[i] = B[i - D] + power

    for r in R[H+1:]:
        le, ri = (int(i) for i in r.split())
        print(B[ri] - B[le])


if __name__ == '__main__':
    main()
