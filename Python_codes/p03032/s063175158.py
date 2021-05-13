def resolve():
    N, K = list(map(int, input().split()))
    V = list(map(int, input().split()))
    start = (K+1)//2 if K%2==1 else K//2
    maxvalue = 0
    for npop in range(start, K+1):
        if npop >= N:
            npush = K - N
            negs = sorted([v for v in V if v < 0])
            posis = [v for v in V if v >= 0]
            maxvalue = max(maxvalue, sum(posis)+(sum(negs)-sum(negs[:npush])))
            continue

        for nleft in range(npop+1):
            nright = npop-nleft
            picked = V[:nleft] + V[N-nright:]
            negs = sorted([v for v in picked if v < 0])
            posis = [v for v in picked if v >= 0]
            npush = min(K-npop, len(negs))
            maxvalue = max(maxvalue, sum(posis)+(sum(negs)-sum(negs[:npush])))
    print(maxvalue)
            


if '__main__' == __name__:
    resolve()