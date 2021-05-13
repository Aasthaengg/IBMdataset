def main():
    N, M, Q = map(int, input().split())
    LR = [[0] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        l, r = map(int, input().split())
        l, r = l - 1, r - 1
        LR[0][r] += 1
        LR[l + 1][r] -= 1
    for r in range(N):
        t = 0
        for l in range(N):
            t += LR[l][r]
            LR[l][r] = t
    for l in range(N):
        t = 0
        for r in range(N):
            t += LR[l][r]
            LR[l][r] = t
    for _ in range(Q):
        p, q = map(int, input().split())
        p, q = p - 1, q - 1
        print(LR[p][q])
main()
