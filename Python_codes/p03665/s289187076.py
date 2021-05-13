import collections
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N,P = map(int,input().split())
A = list(map(int,input().split()))
H = [i%2 for i in A]
B = collections.Counter(H)[1]

ans = 0
for i in range(1,B//2+1):
    ans += combinations_count(B, 2*i)
C = (ans+1) * (2**(len(A)-B))
print(C if P == 0 else 2**N - C)