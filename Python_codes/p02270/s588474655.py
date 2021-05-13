def checkCapacity(W,k,P):
    ws = 0
    cnt = 1
    for wi in W:
        if wi > P: return False
        ws += wi
        if ws > P:
            cnt += 1
            ws = wi
        if cnt > k: return False
    return True

if __name__=='__main__':
    n,k = list(map(int, input().split()))
    W = list(map(int,[input() for _ in range(n)]))
    Pmax = sum(W)
    Pmin = 0
    while Pmin < Pmax:
        P = (Pmax + Pmin) // 2
        if checkCapacity(W,k,P):
            Pmax = P
        else:
            Pmin = P + 1
    print(Pmax)