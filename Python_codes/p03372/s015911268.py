def main():
    N, C = map(int, input().split())
    sushis = [(0, 0) for _ in range(N)]
    for i in range(N):
        x, v = map(int, input().split())
        sushis[i] = (x, v)
    ls, rs = 0, 0
    left = [(0, 0) for _ in range(N+1)]
    right = [(0, 0) for _ in range(N+1)]
    for i in range(N):
        ls += sushis[i][1]
        lx = sushis[i][0]
        rs += sushis[-i-1][1]
        rx = C - sushis[-i-1][0]
        left[i+1] = (max(ls-lx, left[i][0]),
                     max(ls-lx*2, left[i][1]))
        right[i+1] = (max(rs-rx, right[i][0]),
                      max(rs-rx*2, right[i][1]))
    ans = 0
    for i in range(N+1):
        ans = max([left[i][0] + right[N-i][1],
                   left[i][1] + right[N-i][0],
                   ans])
    print(ans)


if __name__ == "__main__":
    main()
