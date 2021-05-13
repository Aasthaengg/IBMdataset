import sys
input = sys.stdin.readline
import math


def read():
    N = int(input().strip())
    X = input().strip()
    return N, X


def bitdiv(N:int, X:str, d:int):
    q = 0
    for i in range(N):
        q <<= 1
        q |= int(X[i])
        p, q = divmod(q, d)
    return q


def solve(N, X):
    BP = [0 for i in range(N)]
    BM = [0 for i in range(N)]

    c = X.count("1")
    

    # 2^k mod (c+1) を高速に求める
    qp = int(X, base=2) % (c+1)
    BP[N-1] = 1 % (c+1)
    for i in range(N-2, -1, -1):
        BP[i] = (BP[i+1] * 2) % (c+1)
    
    # 2^k mod (c-1) を高速に求める
    if c > 1:
        qm = int(X, base=2) % (c-1)
        BM[N-1] = 1 % (c-1)
        for i in range(N-2, -1, -1):
            BM[i] = (BM[i+1] * 2) % (c-1)

    for i in range(N):
        q = 0
        ans = 0
        if X[i] == "0":
            # X_i \equiv (X + 2^i)
            q = (qp + BP[i]) % (c+1)
            ans += 1
        elif X[i] == "1" and c > 1:
            # X_i \equiv (X - 2^i)
            q = (qm - BM[i]) % (c-1)
            ans += 1
        else:
            q = 0
            ans = 0
        while q > 0:
            q %= (bin(q).count("1"))
            ans += 1
        print(ans)


if __name__ == '__main__':
    inputs = read()
    outputs = solve(*inputs)
    if outputs is not None:
        print("%s" % str(outputs))
