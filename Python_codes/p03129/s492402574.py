import math


def solution(N, K):
    if (math.floor((N + 1) / 2) >= K):
        return "YES"
    else:
        return "NO"


n, k = [int(s) for s in input().split(' ')]
print(solution(n, k))
