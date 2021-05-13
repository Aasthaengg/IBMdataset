import math

N, M = map(int, input().split())
p = 10**9 + 7
n_kai = math.factorial(N) % p
m_kai = math.factorial(M) % p
if abs(N - M) > 1:
    print(0)
elif abs(N - M) == 1:
    print(n_kai * m_kai % p)
else:
    print(2*n_kai*m_kai % p)
