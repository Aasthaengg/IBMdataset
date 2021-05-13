import sys

N = int(input())
A = list(map(int, sys.stdin.readline().rsplit()))

n = max(A)

if n % 2 == 0:
    nn = n // 2
else:
    nn = (n + 1) // 2

minA = n
aa = n
for a in A:
    if abs(a - nn) <= minA:
        minA = abs(a - nn)
        aa = a
print(n, aa)
