from math import comb
n, p = list(map(int, input().split()))
a = list(map(int, input().split()))

n0 = 0
n1 = 0

for i in range(n):
    if a[i] % 2 == 0:
        n0 += 1
    else:
        n1 += 1

x = 0
if p == 0:
    for i in range(0, n1+1, 2):
        x += comb(n1, i)
else:
    for i in range(1, n1+1, 2):
        x += comb(n1, i)

print(2**n0 * x)