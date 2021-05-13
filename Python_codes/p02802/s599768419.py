def resolve():
    N, M = list(map(int, input().split()))
    ACs = [0 for _ in range(N)]
    WAs = [0 for _ in range(N)]
    for _ in range(M):
        p, result = list(input().split())
        p = int(p)
        if result == "AC":
            ACs[p-1] += 1
        else:
            if ACs[p-1] == 0:
                WAs[p-1] += 1
    nac = 0
    nwa = 0
    for i in range(N):
        if ACs[i] >= 1:
            nac += 1
            nwa += WAs[i]
    print(nac, nwa)


if '__main__' == __name__:
    resolve()