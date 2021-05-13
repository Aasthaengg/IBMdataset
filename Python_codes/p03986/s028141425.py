X = list(input())
N = len(X)
NHALF = N // 2

def solve():
    nt, ns = 0, 0
    for i in range(N):
        if X[i] == 'S':
            ns += 1
        elif ns > 0:
            ns -= 1
        else:
            nt += 1
    return nt + ns


print(solve())