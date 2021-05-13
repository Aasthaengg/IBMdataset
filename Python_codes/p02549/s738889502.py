def main():
    N, K = map(int, input().split())
    MOD = 998244353

    S = []
    LR = []
    for i in range(K):
        l, r = map(int, input().split())
        LR.append((l, r))
    
    LR.sort()
    # for (l, r) in LR:
    #     for x in range(l, min(r+1, N)):
    #         S.append(x)

    a = [0] * N
    f = [0] * N
    f[0] = 1
    a[1] = -1

    for i in range(N):
        if i > 0:
            f[i] = (f[i-1] + a[i]) % MOD
        for (l, r) in LR:
            if i+l < N:
                a[i+l] = (a[i+l] + f[i]) % MOD
            if i+r+1 < N:
                a[i+r+1] = (a[i+r+1] - f[i]) % MOD
    # print(f)
    print(f[N-1])

if __name__ == '__main__':
    main()