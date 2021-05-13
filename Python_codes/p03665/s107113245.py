N, P = map(int, input().split())
A = list(map(int, input().split()))

import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def calc(n):
    ans = 0
    for r in range(n-n%2, -1, -2):
        ans += combinations_count(n, r)
    return ans
    
gusu = 0
for a in A:
    if a%2 == 0:
        gusu +=1
kisu = N - gusu

p0 = 2**gusu*calc(kisu)
if P == 0:
    print(p0)
else:
    print(2**N-p0)
