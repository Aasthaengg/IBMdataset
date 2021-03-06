import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import accumulate


def read():
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    return N, M, A

def solve(N, M, A):
    D = defaultdict(int)
    S = [0 for i in range(N+1)]
    for i in range(N):
        s = (S[i] + A[i]) % M
        S[i+1] = s
        D[s] += 1
    ans = 0
    k = 0
    for i in range(N):
        ans += D[k]
        k += A[i]
        k %= M
        D[k] -= 1
    return ans


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
