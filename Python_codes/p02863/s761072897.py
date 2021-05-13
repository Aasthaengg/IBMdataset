import itertools


def read():
    N, T = list(map(int, input().strip().split()))
    A = list()
    B = list()
    for i in range(N):
        a, b = list(map(int, input().strip().split()))
        A.append(a)
        B.append(b)
    return N, T, A, B


def solve(N, T, A, B):
    dp1 = [[0 for j in range(T)] for i in range(N+2)]
    dp2 = [[0 for j in range(T)] for i in range(N+2)]
    for i, t in itertools.product(range(N), range(T)):
        u = t - A[i]
        if u >= 0:
            dp1[i+1][t] = max(dp1[i][u] + B[i], dp1[i][t])
        else:
            dp1[i+1][t] = dp1[i][t]
        u = t - A[N-1-i]
        if u >= 0:
            dp2[N-i][t] = max(dp2[N+1-i][u] + B[N-1-i], dp2[N+1-i][t])
        else:
            dp2[N-i][t] = dp2[N+1-i][t]
    v = 0
    for i, t in itertools.product(range(N), range(T)):
        v = max(v, dp1[i][t] + dp2[i+2][(T-1) - t] + B[i])
    return v


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
