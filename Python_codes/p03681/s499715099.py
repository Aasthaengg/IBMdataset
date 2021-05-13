# ABC065 C Reconciled?

import math

n, m = map(int, input().split())
A = 10**9 + 7

if abs(n-m) > 1:
    print("0")
elif n == m:
    print(((math.factorial(m)**2)*2)%A)
else:
    print((math.factorial(m)*math.factorial(n))%A)