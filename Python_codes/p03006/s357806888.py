import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    if N==1:
        print(1)
    else:
        X, Y = [0] * N, [0] * N
        for i in range(N):
            X[i], Y[i] = map(int, input().split())
        ans = 10 ** 10
        for i in range(N):
            for j in range(N):
                if i != j:
                    p = X[j] - X[i]
                    q = Y[j] - Y[i]
                else:
                    continue
                sub = 0
                for k in range(N):
                    for l in range(N):
                        if X[l] - X[k] == p and Y[l] - Y[k] == q:
                            sub += 1
                ans = min(ans, N - sub)
    
        print(ans)


resolve()