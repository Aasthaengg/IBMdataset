import bisect

A, B, Q = map(int,input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]

for _ in range(Q):
    x = int(input())
    a = bisect.bisect_left(S,x)
    b = bisect.bisect_left(T,x)
    a1 = float("inf")
    a2 = float("inf")
    b1 = float("inf")
    b2 = float("inf")
    
    if a == 0:
        a2 = S[a] - x
    elif a == A:
        a1 = x - S[a-1]
    else:
        a1 = x - S[a-1]
        a2 = S[a] - x
    if b == 0:
        b2 = T[b] - x
    elif b == B:
        b1 = x - T[b-1]
    else:
        b1 = x - T[b-1]
        b2 = T[b] - x
    
    print(min(max(a1,b1),max(a2,b2), min(a1,b2)*2+max(a1,b2), min(a2,b1)*2+max(a2,b1)))