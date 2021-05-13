N, M = map(int, input().split())

import math
if M >= 2:
    m = math.factorial(M) // (math.factorial(M - 2) * math.factorial(2))
else:
    m = 0
if N >= 2:
    n = math.factorial(N) // (math.factorial(N - 2) * math.factorial(2))
else:
    n = 0
print(m + n)