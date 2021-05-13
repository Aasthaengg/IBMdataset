import math

N, M = map(int, input().split())
if abs(N - M) == 0:
    print(math.factorial(N) * math.factorial(M) * 2 % (10 ** 9 + 7))
elif abs(N - M) == 1:
    print(math.factorial(N) * math.factorial(M) % (10 ** 9 + 7))
else:
    print(0)
