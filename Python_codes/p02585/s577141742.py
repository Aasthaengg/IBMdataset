N, K = [int(_) for _ in input().split()]
P = [int(_) - 1 for _ in input().split()]
C = [int(_) for _ in input().split()]


X = [False for _ in range(N)]

V = []
for i in range(N):
    if X[i]:
        continue
    t = i
    v = []
    while X[t] is False:
        X[t] = True
        v.append(C[t])
        t = P[t]
    V.append(tuple(v))

def f(v, K):
    if K == 0:
        return 0
    if max(v) < 0:
        return max(v)
    n = len(v)

    X = [0]
    for i in range(n):
        X.append(X[-1] + v[i])
    ans = -100000000000
    for i in range(n + 1):
        for j in range(i):
            if i - j > K:
                continue
            ans = max(ans, X[i] - X[j])
    return(ans)

ans = -100000000000
for v in V:
    n = len(v)
    if K > n:
        s = sum(v)
        if s > 0:
            x = s * (K // n) + f(v * 2, K % n)
            y = s * (K // n - 1) + f(v * 2, n)
            a = max(x, y)
        else:
            a = f(v * 2, n)
    else:
        a = f(v * 2, K)
    ans = max(a, ans)

print(ans)
