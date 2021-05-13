N, K = map(int, input().split())
A = list(map(int, input().split()))

idx = A.index(1)

ans = N
for k in range(K + 1):
    L = idx - (K - k - 1)
    R = (N - 1 - idx) - k
    cntL = 0
    cntR = 0
    while L > 0:
        cntL += 1
        L -= K - 1
    while R > 0:
        cntR += 1
        R -= K - 1
    ans = min(ans, cntL + cntR + 1)

print(ans)
