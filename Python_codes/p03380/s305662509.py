from itertools import combinations
n = int(input())
a = [int(i) for i in input().split()]
a.sort()

ai = a[-1]
aj = -1
for i in range(n-1):
    if abs(a[i] - ai/2) <= abs(aj - ai/2):
        aj = a[i]
print(ai, aj)