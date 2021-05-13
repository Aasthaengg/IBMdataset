from math import factorial as frac

N, M = map(int, input().split())

INF = 10**9 + 7

if abs(N-M) > 1:
    print(0)
elif abs(N-M) == 1:
    print(frac(N)*frac(M)%INF)
else:
    print(((frac(N)*frac(M))*2)%INF)
