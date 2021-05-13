def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    return table
from bisect import *
N, M = map(int, input().split())
A = divisors(M)
A.sort()
print(M//A[bisect_left(A,N)])