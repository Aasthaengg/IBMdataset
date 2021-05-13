import math
N, M = map(int, input().split())
a = abs(N-M)
b = math.factorial(N)*math.factorial(M)
c = 10**9+7
if a>1:
    print(0)
elif a==1:
    print(b%c)
else:
    print(2*b%c)
