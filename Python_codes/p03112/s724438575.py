A,B,Q = map(int,input().split())
S = [int(input()) for _ in range(A)]

T = [int(input()) for _ in range(B)]

from bisect import bisect_left

for _ in range(Q):
    ans = 10**12
    x = int(input())
    idxs = bisect_left(S,x)
    idxt = bisect_left(T,x)

    if idxs < A and idxt < B:
        ans = min(ans, max(S[idxs],T[idxt])-x)
    if 0 <= idxs-1 and 0 <= idxt-1:
        ans = min(ans, x-min(S[idxs-1],T[idxt-1]))
    if idxs < A and 0 <= idxt-1:
        ans = min(ans, S[idxs]-T[idxt-1] + min(S[idxs]-x, x-T[idxt-1]))
    if idxt < B and 0 <= idxs-1:
        ans = min(ans, T[idxt]-S[idxs-1] + min(T[idxt]-x, x-S[idxs-1]))
    print(ans)
