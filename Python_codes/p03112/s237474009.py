import bisect
A, B, Q = map(int, input().split())

S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
X = [int(input()) for _ in range(Q)]

bLeft = bisect.bisect_left

for x in X:
    si = bLeft(S, x)
    sleft = float('inf')
    sright = float('inf')
    if si != 0:
        sleft = x-S[si-1]
    if si != A:
        sright = S[si]-x

    ti = bLeft(T, x)
    tleft = float('inf')
    tright = float('inf')
    if ti != 0:
        tleft = x-T[ti-1]
    if ti != B:
        tright = T[ti]-x

    ans1 = max(sleft, tleft)
    ans2 = max(sright, tright)
    ans3 = min(min(sleft, sright), min(tleft, tright)) + min(sleft, sright) + min(tleft, tright)
    print(min(ans1, ans2, ans3))
