from math import factorial

N, M = map(int, input().split())

a = 10**9+7
if abs(N-M) >= 2:
    print(0)

elif N == M:
    print((2*factorial(N)*factorial(M)) % a)

else:
    print((factorial(N)*factorial(M)) % a)
