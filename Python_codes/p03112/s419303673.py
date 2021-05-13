import bisect
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]

def D(a,b,c):
    return abs(a-b) + abs(b-c)

def getAns(x):
    ret = 10**18
    U = [S, T]
    for k in range(len(U)):
        u = U[k]
        v = U[(k-1)%2]
        idx = bisect.bisect_left(u, x)
        for i in [idx-1, idx]:
            if not 0<=i<len(u):
                continue
            idxx = bisect.bisect_left(v, u[i])
            for j in [idxx-1, idxx]:
                if 0<=j<len(v):
                    ret = min(ret, D(x, u[i], v[j]))
    return ret

for x in X:
    print(getAns(x))



