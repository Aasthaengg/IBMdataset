from bisect import bisect_right
INFTY = 10**11
A,B,Q = map(int,input().split())
S = [int(input()) for _ in range(A)]
S.insert(0,-INFTY)
S.append(INFTY)
T = [int(input()) for _ in range(B)]
T.insert(0,-INFTY)
T.append(INFTY)
for _ in range(Q):
    x = int(input())
    indS = bisect_right(S,x)
    indT = bisect_right(T,x)
    d1 = x-S[indS-1]+abs(S[indS-1]-T[indT-1])
    d2 = x-S[indS-1]+abs(S[indS-1]-T[indT])
    d3 = S[indS]-x+abs(S[indS]-T[indT-1])
    d4 = S[indS]-x+abs(S[indS]-T[indT])
    d5 = x-T[indT-1]+abs(T[indT-1]-S[indS-1])
    d6 = x-T[indT-1]+abs(T[indT-1]-S[indS])
    d7 = T[indT]-x+abs(T[indT]-S[indS-1])
    d8 = T[indT]-x+abs(T[indT]-S[indS])
    print(min(d1,d2,d3,d4,d5,d6,d7,d8))