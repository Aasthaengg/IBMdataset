def main():
    H, W = map(int, input().split())
    g = []
    q = []
    cnt = 0
    for h in range(H):
        A = str(input())
        row = []
        for w in range(W):
            row.append(A[w])
            if A[w] == '#':
                cnt += 1
                q.append([h, w])
        g.append(row)
    ans = 0
    dh = [1, 0, 0, -1]
    dw = [0, -1, 1, 0]
    while cnt < H * W:
        ans += 1
        nextq = []
        while q:
            h, w = q.pop()
            for i in range(4):
                nh = h + dh[i]
                nw = w + dw[i]
                if 0 <= nh < H and 0 <= nw < W and g[nh][nw] == '.':
                    g[nh][nw] = '#'
                    nextq.append([nh, nw])
                    cnt += 1
        q = nextq
    print(ans)
main()
