import bisect
A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]

for x in X:
    SL, SR, TL, TR = 10**20, 10**20, 10**20, 10**20
    i = bisect.bisect_left(S, x)
    if i != 0:
        SL = x-S[i-1]
    if i != A:
        SR = S[i]-x

    j = bisect.bisect_left(T, x)
    if j != 0:
        TL = x-T[j-1]
    if j != B:
        TR = T[j]-x

    ans = min(max(SL, TL), min(2*SL+TR, SL+2*TR),
              min(2*TL+SR, TL+2*SR), max(SR, TR))
    print(ans)
