from math import gcd
N = int(input())
A = list(map(int, input().split()))

while len(A) > 1:
    A.append(gcd(A.pop(), A.pop()))
print(A[0])
