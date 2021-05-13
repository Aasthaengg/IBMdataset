from decimal import *

k_str = input()
k = Decimal(k_str)
n = 50

A = [0] * (n)
pl = k // n

amari = k % n
kakanai = n - amari
start = (n + 1 - amari) % (n+1)
ind = 0

print(n)
for i in range(n+1):
    if start != kakanai:
        A[ind] = start + pl
        ind += 1
    start = (start + 1) % (n+1)

print(" ".join(map(str, A)))