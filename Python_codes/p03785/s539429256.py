import sys
input = sys.stdin.readline
from itertools import accumulate


def read():
    
    N, C, K = map(int, input().strip().split())
    T = []
    for i in range(N):
        t = int(input().strip())
        T.append(t)
    return N, C, K, T


def solve(N, C, K, T):
    T.sort()
    i = 0
    ans = 0
    while i < N:
        tk = T[i] + K
        j0 = i
        for j in range(j0, min(j0+C, N)):
            if T[j] <= tk:
                i += 1
            else:
                break
        ans += 1
    return ans


if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
