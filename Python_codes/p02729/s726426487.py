import math
A,B = map(int,input().split())
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

if ((A<=1) and (B<=1)):
    print(0)
    exit()
if (B<=1):
    print(combinations_count(A,2))
    exit()
if (A<=1):
    print(combinations_count(B,2))
    exit()
print(combinations_count(A,2)+combinations_count(B,2))
