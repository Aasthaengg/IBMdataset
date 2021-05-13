def main():
    H, W, K = map(int, input().split())
    u = [1] + [0] * (W - 1)
    mod = 10**9 + 7
    def cw(n):
        if n == 0:
            return 0
        if n == 1:
            return 2
        return cw(n - 2) + cw(n - 1) 
    CW = [1, 2, 3, 5, 8, 13, 21, 34, 55, 1, 1, 1]

    for _ in range(H):
        v = [0] * W
        for w in range(W):
            t = 0
            if w >= 1:
                t += u[w - 1] * CW[w - 2] * CW[W - w - 2]
            t += u[w] *     CW[w - 1] * CW[W - w - 2]
            if w < W - 1:
                t += u[w + 1] * CW[w - 1] * CW[W - w - 3]
            v[w] = t % mod
        u = v
    print(u[K - 1])

main()
