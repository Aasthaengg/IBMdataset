from bisect import bisect_left,bisect_right
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
A,B,Q = map(int,input().split())
S = []
T = []
for i in range(A):
    S.append(int(input()))
for i in range(B):
    T.append(int(input()))
for i in range(Q):
    x = int(input())
    values = []
    p1 = bisect_left(S,x)
    if p1 == 0:
        p2 = bisect_left(T,S[p1])
        if p2 == 0:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
        elif p2 == B:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
        else:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
    elif p1 == A:
        p1 -= 1
        p2 = bisect_left(T,S[p1])
        if p2 == 0:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
        elif p2 == B:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
        else:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
    else:
        #-1
        p1 -= 1
        p2 = bisect_left(T,S[p1])
        if p2 == 0:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
        elif p2 == B:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
        else:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
        p1 += 1
        p2 = bisect_left(T,S[p1])
        if p2 == 0:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
        elif p2 == B:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))
        else:
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2]))
            values.append(abs(x-S[p1])+abs(S[p1]-T[p2-1]))

    p1 = bisect_left(T,x)
    if p1 == 0:
        p2 = bisect_left(S,T[p1])
        if p2 == 0:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
        elif p2 == A:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
        else:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
    elif p1 == B:
        p1 -= 1
        p2 = bisect_left(S,T[p1])
        if p2 == 0:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
        elif p2 == A:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
        else:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
    else:
        #-1
        p1 -= 1
        p2 = bisect_left(S,T[p1])
        if p2 == 0:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
        elif p2 == A:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
        else:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
        p1 += 1
        p2 = bisect_left(S,T[p1])
        if p2 == 0:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
        elif p2 == A:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
        else:
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2]))
            values.append(abs(x-T[p1])+abs(T[p1]-S[p2-1]))
    d = min(values)
    print(d)
