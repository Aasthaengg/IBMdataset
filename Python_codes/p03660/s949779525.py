def main():
    N = int(input())
    E = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        E[a - 1].append(b - 1)
        E[b - 1].append(a - 1)
    C = [0] * N
    B = set([0])
    W = set([N - 1])
    C[0] = 1
    C[-1] = -1
    while B or W:
        BN = set()
        for b in B:
            for bb in E[b]:
                if bb != b and C[bb] == 0:
                    C[bb] = 1
                    BN.add(bb)
        B = BN
        WN = set()
        for w in W:
            for ww in E[w]:
                if ww != w and C[ww] == 0:
                    C[ww] = -1
                    WN.add(ww)
        W = WN
    return 'Fennec' if C.count(1) > C.count(-1) else 'Snuke'

print(main())
