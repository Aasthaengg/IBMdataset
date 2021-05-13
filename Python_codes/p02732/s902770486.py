import collections
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
N = int(input())
A = list(map(int,input().split()))
B = collections.Counter(A)
num = 0
for i in set(A):
    if B[i] > 1:
        num += combinations_count(B[i], 2)
for i in A:
    print(num-B[i]+1)