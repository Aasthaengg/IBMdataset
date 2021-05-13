import math
N, K = map(int, input().split())
h = list(map(int, input().split()))
 
def nya(N, K, h):
    S = [0] * N
    S[0] = 0
 
    for i in range(1, N):
        value = math.inf
        for step in range(1, K + 1):
            if i - step < 0:
                break
            value = min(value, S[i - step] + abs(h[i] - h[i - step]))
        S[i] = value
    return S[N-1]

print(nya(N, K, h))